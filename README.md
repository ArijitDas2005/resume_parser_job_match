# Resume Parser & Job Match System

An intelligent tool that automates resume screening using Natural Language Processing. Upload a PDF resume, extract key sections, and compare with job descriptions to calculate a match score.

## 💡 Features

- Upload resume in PDF format
- Parse and extract skills, experience, and education
- Input job description directly
- Match percentage calculation using NLP
- Clean web interface with result display

## 🛠 Tech Stack

- Python, Flask
- spaCy for NLP
- PyMuPDF for PDF parsing
- Pandas, scikit-learn
- HTML/CSS (Jinja templates)

## 📦 Installation

```bash
git clone https://github.com/ArijitDas2005/resume-parser-jobmatch.git
cd resume-parser-jobmatch
pip install -r requirements.txt
python app.py


Then visit: http://localhost:5000


Example:
1. Upload resume.pdf
2. Paste job description
3. Click "Analyze"
4. View match percentage and extracted keywords

📁 Project Structure
├── app.py           # Flask app entry point
├── parser.py        # Resume/JD parsing logic
├── templates/
│   └── index.html   # Web interface
├── static/          # (optional styles/images)
└── requirements.txt


