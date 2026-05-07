from fastapi import FastAPI, HTTPException
import pickle

app = FastAPI()

# Load model and vectorizer
model = pickle.load(open('model/spam_model.pkl', 'rb'))
vectorizer = pickle.load(open('model/vectorizer.pkl', 'rb'))

# Root endpoint (visible in browser)
@app.get("/")
def home():
    return {
        "message": "Spam Classifier API is running",
        "usage": "Send POST request to /predict with JSON: { 'text': 'your message' }"
    }

# Prediction endpoint
@app.post("/predict")
def predict(data: dict):
    # Validate input
    if "text" not in data:
        raise HTTPException(status_code=400, detail="Missing 'text' field")

    text = data["text"]

    # Convert text → features
    vector = vectorizer.transform([text])
    
    prediction = model.predict(vector)[0]

    return {
        "input_text": text,  
        "prediction": int(prediction),
        "label": "spam" if prediction == 1 else "not spam"
    }