# 🔒 Sensitive Data Detection & Compliance Assistant

## 📌 Project Overview

This project is an AI-powered Sensitive Data Detection & Compliance Assistant developed using Python and Streamlit. It allows users to upload PDF, TXT, or CSV documents, automatically detects sensitive information, classifies the document based on risk level, and helps improve data security awareness.

---

## 🚀 Features

- Upload PDF, TXT, and CSV files
- Extract text from uploaded documents
- Detect sensitive information using Regular Expressions
- Detect:
  - Email Addresses
  - Phone Numbers
  - Aadhaar Numbers
  - PAN Numbers
  - Credit Card Numbers
  - API Keys
  - Passwords
  - Employee IDs
- Classify documents into Low, Medium, or High Risk
- Simple and user-friendly Streamlit interface

---

## 🛠️ Tech Stack

- Python
- Streamlit
- Pandas
- PyPDF
- Regular Expressions (Regex)
- OpenAI API (Planned)
- LangChain (Future Enhancement)
- FAISS (Future Enhancement)

---

## 📂 Project Structure

```
Sensitive-Data-Assistant/
│
├── app.py
├── detector.py
├── utils.py
├── rag.py
├── requirements.txt
├── .env
└── README.md
```

---

## ⚙️ Installation

1. Clone the repository

```bash
git clone https://github.com/yourusername/Sensitive-Data-Assistant.git
```

2. Navigate to the project folder

```bash
cd Sensitive-Data-Assistant
```

3. Install dependencies

```bash
pip install -r requirements.txt
```

4. Add your OpenAI API Key inside the `.env` file

```
OPENAI_API_KEY=your_api_key
```

5. Run the application

```bash
streamlit run app.py
```

---

## 🧠 AI/ML Approach

The application uses Regular Expressions (Regex) to identify different types of sensitive information such as Aadhaar numbers, PAN numbers, email addresses, phone numbers, passwords, API keys, employee IDs, and credit card numbers. A risk score is calculated based on the detected sensitive information, and the document is classified into Low, Medium, or High Risk categories. The application is designed to be extended with OpenAI and Retrieval-Augmented Generation (RAG) for AI-powered compliance summaries and document question answering.

---

## ⚠️ Challenges Faced

- Handling multiple document formats
- Designing accurate regex patterns
- Avoiding false detections
- Creating a simple and responsive Streamlit interface

---

## 🔮 Future Improvements

- AI-generated compliance summary
- Document Question Answering (RAG)
- OCR support for scanned PDFs
- Sensitive data masking
- Audit logging
- Multi-document analysis
- Docker deployment
- Cloud deployment

---

## 📷 Sample Output

The application displays:

- Extracted Document Text
- Sensitive Information Detected
- Risk Classification

---

## 👨‍💻 Author

**Srinath Vemula**

---

## 📄 License

This project was developed as part of an AI Research Innovation Internship assignment.
