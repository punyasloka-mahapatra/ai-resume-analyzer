# 📄 AI Resume Analyzer (with Machine Learning)

## 🚀 Overview
The **AI Resume Analyzer** is a Streamlit-based web application that extracts text from resumes (PDF/DOCX), identifies key skills, and evaluates how well a resume matches a job description using **Scikit-Learn's TF-IDF and Cosine Similarity**.

## 🔥 Features
✅ Upload **PDF/DOCX** resumes for analysis  
✅ Extract text and **identify skills** from resumes  
✅ Paste a **job description** for comparison  
✅ Uses **TF-IDF & Cosine Similarity** for accurate job matching  
✅ **Streamlit-based UI** for easy interaction

## 📦 Installation

1. **Clone the Repository** (if using GitHub)
   ```sh
   git clone https://github.com/punyasloka-mahapatra/ai-resume-analyzer
   cd ai-resume-analyzer
   ```

2. **Install Dependencies**
   ```sh
   pip install -r requirements.txt
   python -m spacy download en_core_web_sm
   ```

## ▶️ How to Run

Run the following command to start the web app:
```sh
streamlit run app.py
```

Then, open the **localhost link** in your browser to use the app!

## 🛠️ Technologies Used
- **Python** (Core programming language)
- **Streamlit** (Web application framework)
- **PDFPlumber** (Extracts text from PDF resumes)
- **Python-Docx** (Extracts text from DOCX resumes)
- **SpaCy** (Performs NLP tasks like named entity recognition)
- **Scikit-Learn** (TF-IDF & Cosine Similarity for job matching)

## 📌 Usage
1. **Upload a Resume (PDF/DOCX)**
2. **View extracted text and identified skills**
3. **Paste a job description in the sidebar**
4. **Get a job match percentage**

## 💡 Future Enhancements
- 🤖 **Machine Learning-based skill extraction**
- 📊 **More advanced job-resume matching algorithms**
- 🏆 **Resume ranking for multiple job descriptions**

## 📧 Contact
For any questions or suggestions, feel free to reach out at **punyasloka.mahapatra@myyahoo.com**.

---

**Enjoy analyzing resumes with AI! 🚀**

