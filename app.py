from flask import Flask, request, render_template
from parser import extract_resume_data
from matcher import calculate_match

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    match_score = None
    resume_data = {}

    if request.method == 'POST':
        file = request.files['resume']
        job_description = request.form['job_desc']
        
        if file.filename.endswith('.pdf'):
            resume_data = extract_resume_data(file)
            match_score = calculate_match(resume_data['skills'], job_description)

    return render_template('index.html', score=match_score, resume=resume_data)

if __name__ == '__main__':
    app.run(debug=True)
