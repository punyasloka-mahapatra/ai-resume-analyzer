import streamlit as st
import pdfplumber
import docx
import spacy
import os
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

nlp = spacy.load("en_core_web_sm")

def extract_text_from_pdf(pdf_file):
    with pdfplumber.open(pdf_file) as pdf:
        text = "\n".join([page.extract_text() for page in pdf.pages if page.extract_text()])
    return text


def extract_text_from_docx(docx_file):
    doc = docx.Document(docx_file)
    return "\n".join([para.text for para in doc.paragraphs])


def extract_skills(text):
    skills = ["Java", "Python", "AWS", "Spring Boot", "Docker", "Kubernetes", "CI/CD"]
    found_skills = [skill for skill in skills if skill.lower() in text.lower()]
    return found_skills


def calculate_resume_match(resume_text, job_description):
    vectorizer = TfidfVectorizer()
    tfidf_matrix = vectorizer.fit_transform([resume_text, job_description])
    similarity_score = cosine_similarity(tfidf_matrix[0], tfidf_matrix[1])[0][0]
    return round(similarity_score * 100, 2)


st.title("📄 AI Resume Analyzer (with ML)")

st.sidebar.header("Upload Resume")
uploaded_file = st.sidebar.file_uploader("Choose a resume (PDF/DOCX)", type=["pdf", "docx"])

if uploaded_file:
    file_extension = os.path.splitext(uploaded_file.name)[1]


    if file_extension == ".pdf":
        resume_text = extract_text_from_pdf(uploaded_file)
    elif file_extension == ".docx":
        resume_text = extract_text_from_docx(uploaded_file)
    else:
        st.error("Unsupported file format.")
        st.stop()

    st.subheader("Extracted Resume Content")
    st.text_area("Resume Text", resume_text, height=200)


    skills = extract_skills(resume_text)
    st.subheader("Extracted Skills")
    st.write("✅ **Skills Found:**", ", ".join(skills) if skills else "No skills detected.")

    st.sidebar.header("Job Description")
    job_description = st.sidebar.text_area("Paste Job Description Here")

    if job_description:
        match_score = calculate_resume_match(resume_text, job_description)
        st.subheader("Job Match Score")
        st.write(f"✅ **Match Percentage:** {match_score}%")
