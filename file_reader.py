import fitz  # PyMuPDF
import docx
import pytesseract
from PIL import Image
import cv2
import os
import chardet
pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"


def read_txt(file_path):
 try:
    with open(file_path, 'rb') as f:
            raw_data = f.read()
            encoding = chardet.detect(raw_data)['encoding'] or 'utf-8'
    with open(file_path, 'r', encoding=encoding) as f:
        return f.read()
 except Exception as e:
        raise ValueError(f"Error reading text file: {e}")

def read_docx(file_path):
 try:
    doc1= docx.Document(file_path)
    return '\n'.join([para.text for para in doc1.paragraphs])
 except Exception as e:
        raise ValueError(f"Error reading docx: {e}")

def read_pdf(file_path):
 try:
    doc = fitz.open(file_path)
    text = ''
    for page in doc:
        text += page.get_text()
    doc.close()  
    return text
 except Exception as e:
        raise ValueError(f"Error reading PDF: {e}")
def read_image(file_path):
 try:
    # Load and preprocess image
    img = cv2.imread(file_path)
    if img is None:
        raise ValueError("Could not load image")
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    _, thresh = cv2.threshold(gray, 150, 255, cv2.THRESH_BINARY)

    #noise reduction
    denoised = cv2.medianBlur(thresh, 3)
    pil_img = Image.fromarray(denoised)
    text = pytesseract.image_to_string(pil_img)
    return text
 except Exception as e:
        raise ValueError(f"Error processing image: {e}")

def extract_text(file_path):
    ext = os.path.splitext(file_path)[-1].lower()
    if ext == '.txt':
        return read_txt(file_path)
    elif ext == '.docx':
        return read_docx(file_path)
    elif ext == '.pdf':
        return read_pdf(file_path)
    elif ext in ['.jpg', '.jpeg', '.png']:
        return read_image(file_path)
    else:
        raise ValueError(f"Unsupported file type: {ext}")
