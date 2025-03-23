# 🌟 AI Resume Analyzer

AI Resume Analyzer is a **Streamlit-based web application** that evaluates resumes by comparing them against a given job description. It calculates a similarity score using **TF-IDF vectorization** and **Cosine Similarity**, helping job seekers understand how well their resume fits a specific job role.

---

## 🚀 Features
✅ Upload resumes in **PDF** or **DOCX** format.  
✅ Enter a job description to compare against the resume.  
✅ Uses **TF-IDF Vectorization** and **Cosine Similarity** to compute a relevance score.  
✅ Provides a **resume score (0-100%)** and a **fit status** (Fits Well / Needs Improvement).  
✅ User-friendly **Streamlit UI**.

---

## 🛠️ Installation
### Prerequisites
Ensure you have Python installed (>=3.7). Install the required dependencies using:

```bash
pip install -r requirements.txt
```

---

## 📌 Usage
Run the Streamlit application:

```bash
streamlit run ai_resume_analyzer.py
```

### Steps to Use
1️⃣ Enter the job description in the provided text area.  
2️⃣ Upload your resume in **PDF** or **DOCX** format.  
3️⃣ Click on **Analyze Resume** to get the score and fit status.

---

## 🔧 Technologies Used
- 🐍 **Python**
- 📊 **Scikit-learn** (for text processing and similarity calculation)
- 🔠 **NLTK** (for text preprocessing)
- 📄 **PDFPlumber & python-docx** (for resume extraction)
- 🎨 **Streamlit** (for UI)

---

## 📊 Example Output
```
Resume Score: 78.5%
Fit Status: Fits Well
```

---

## 📜 License
This project is licensed under the **MIT License**.

---

## 🤝 Contributing
Feel free to **fork** this repository and contribute by submitting **pull requests**.

---

## 👤 Author
Developed by **[Punyasloka Mahapatra]**

## 📬 Contact
💌 **Email**: punyasloka.mahapatra@myyahoo.com
🔗 **LinkedIn**: www.linkedin.com/in/punyasloka-mahapatra-966080148
🐙 **GitHub**: https://github.com/punyasloka-mahapatra

---

🌟 **Star this repository** if you find it useful! 😊
