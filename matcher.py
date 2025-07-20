from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

def calculate_match(resume_skills, job_description):
    vectorizer = TfidfVectorizer()
    combined_text = [' '.join(resume_skills), job_description]
    tfidf = vectorizer.fit_transform(combined_text)
    score = cosine_similarity(tfidf[0:1], tfidf[1:2])
    return round(score[0][0] * 100, 2)
