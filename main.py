from fastapi import FastAPI
from models import TextRequest
from classifiers import Classifier

app = FastAPI()
classifier = Classifier()
classifier.loadModel()

def extract_keywords(text: str):
    words = text.lower().split()
    return list(set(words))[:5]

@app.get("/")   
def read_root():
    return {"message": "Teaa is running!"}


@app.get("/analyzer")
def analyze_text(request: TextRequest):
    if not request.text:
        return {"error": "Text cannot be empty"}

    text = request.text.strip()
    result = classifier.classify(text)                                                              
    keywords = extract_keywords(text)

    return {
        "original_text": text,
        "sentiment": result['label'],
        "confidence": result['score'],
        "word_count": len(text.split()),
        "keywords": keywords
    } 