import os
import pdfplumber
import docx
import numpy as np
import nltk
import streamlit as st
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

nltk.download('punkt')
nltk.download('stopwords')

def extract_text_from_pdf(pdf_path):
    text = ""
    with pdfplumber.open(pdf_path) as pdf:
        for page in pdf.pages:
            text += page.extract_text() + " "
    return text

def extract_text_from_docx(docx_path):
    doc = docx.Document(docx_path)
    return " ".join([para.text for para in doc.paragraphs])

def preprocess_text(text):
    tokens = word_tokenize(text.lower())
    tokens = [word for word in tokens if word.isalnum()]
    tokens = [word for word in tokens if word not in stopwords.words('english')]
    return " ".join(tokens)

def calculate_resume_score(resume_text, job_desc_text):
    vectorizer = TfidfVectorizer()
    vectors = vectorizer.fit_transform([resume_text, job_desc_text])
    similarity_score = cosine_similarity(vectors[0], vectors[1])[0][0] * 100
    return similarity_score

def analyze_resume(resume_path, job_description):
    if resume_path.endswith('.pdf'):
        resume_text = extract_text_from_pdf(resume_path)
    elif resume_path.endswith('.docx'):
        resume_text = extract_text_from_docx(resume_path)
    else:
        return "Unsupported file format. Only PDF and DOCX are supported."

    resume_text = preprocess_text(resume_text)
    job_description = preprocess_text(job_description)

    score = calculate_resume_score(resume_text, job_description)
    fit_status = "Fits Well" if score >= 60 else "Needs Improvement"

    return {
        "Resume Score": round(score, 2),
        "Fit Status": fit_status
    }

st.title("AI Resume Analyzer")
job_description = st.text_area("Enter Job Description")
resume_file = st.file_uploader("Upload Resume (PDF or DOCX)", type=["pdf", "docx"])

if st.button("Analyze Resume"):
    if resume_file and job_description:
        resume_path = f"temp_resume.{resume_file.name.split('.')[-1]}"
        with open(resume_path, "wb") as f:
            f.write(resume_file.read())

        result = analyze_resume(resume_path, job_description)
        st.write(f"**Resume Score:** {result['Resume Score']}%")
        st.write(f"**Fit Status:** {result['Fit Status']}")
        os.remove(resume_path)
    else:
        st.warning("Please upload a resume and enter a job description.")
