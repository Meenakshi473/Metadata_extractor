# 🧠 Metadata Extractor

**AI-powered document analysis tool**  
Extracts metadata from `.pdf`, `.docx`, `.txt`, and image files using NLP and OCR.

---

## 🚀 Features

- 📝 Extract title, author, keywords, summary, entities
- 📥 Upload: PDF, DOCX, TXT, JPG, PNG
- 🧠 Uses KeyBERT, spaCy, HuggingFace Transformers
- 📷 Cloud OCR support for images (OCR.space)
- 📊 Clean, interactive Streamlit UI
- 📁 Download metadata (JSON) and raw text (TXT)

---

## 🖼️ Screenshots

### 🔹 Home Page
![home](screenshots/home.png)

### 🔹 Upload Document & Preview
![upload](screenshots/upload.png)

### 🔹 Extracted Metadata
![metadata](screenshots/metadata.png)

---

## ⚙️ Setup

### 🔧 Requirements

```bash
pip install -r requirements.txt
You also need to get a free OCR API key from OCR.space.
Update it in file_reader.py:
'apikey': 'your_api_key_here'
- **Why:** Guides others to get it running smoothly.

---

### 5. 🧪 **How to Run**
```markdown
**## 🧪 Run the App**

```bash
streamlit run app.py
- **Why:** Quick-start instructions for developers and testers.

---

### 6. 🌐 **Live Demo / Deployment**
```markdown
## 🌐 Live Demo

[Click here to try it on Streamlit Cloud](https://share.streamlit.io/your-app-link)

## 📁 Folder Structure
├── app.py # Streamlit interface
├── file_reader.py # File reading and OCR logic
├── metadata_extractor.py # Metadata extraction logic
├── requirements.txt
├── README.md
└── screenshots/





