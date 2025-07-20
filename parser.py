import fitz  # PyMuPDF
import spacy

nlp = spacy.load("en_core_web_sm")

def extract_text_from_pdf(file):
    doc = fitz.open(stream=file.read(), filetype="pdf")
    text = ""
    for page in doc:
        text += page.get_text()
    return text

def extract_resume_data(file):
    text = extract_text_from_pdf(file)
    doc = nlp(text)
    
    skills = []
    for ent in doc.ents:
        if ent.label_ in ["SKILL", "ORG", "PRODUCT"]:
            skills.append(ent.text.strip().lower())

    return {
        "raw_text": text[:300] + "...",
        "skills": list(set(skills))
    }
