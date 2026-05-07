from fastapi import FastAPI
import pickle

app = FastAPI(title="Spam Classifier API")

model = pickle.load(open("model/spam_model.pkl", "rb"))
vectorizer = pickle.load(open("model/vectorizer.pkl", "rb"))

@app.get("/")
def home():
    return {
        "message": "Spam Classifier API is running successfully 🚀",
        "status": "active",
        "endpoints": {
            "predict": "/predict",
            "docs": "/docs"
        }
    }


@app.post("/predict")
def predict(data: dict):
    text = data["text"]

    vector = vectorizer.transform([text])
    prediction = model.predict(vector)[0]

    return {
        "input_text": text,
        "prediction": int(prediction),
        "label": "spam" if prediction == 1 else "not spam"
    }