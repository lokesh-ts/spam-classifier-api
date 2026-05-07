# Spam Classifier API 

A Machine Learning powered Spam Message Classification API built using FastAPI and Scikit-learn.

## Overview

This project classifies text messages as **Spam** or **Not Spam** using a trained Machine Learning model.
The backend API is developed with FastAPI and deployed on Render for real-time predictions.

---

##  Tech Stack

* Python
* Scikit-learn
* FastAPI
* Uvicorn
* Pickle
* Render

---

##  Project Structure

```bash
spam-classifier/
│
├── model/
│   ├── spam_model.pkl
│   ├── vectorizer.pkl
│
├── app.py
├── requirements.txt
└── README.md
```

---

##  Features

* Spam message prediction
* REST API with FastAPI
* Swagger UI documentation
* Cloud deployment using Render
* TF-IDF text vectorization
* Logistic Regression classifier

---

##  Live API

Backend API:
 https://spam-classifier-api-3hos.onrender.com

Swagger Documentation:
 https://spam-classifier-api-3hos.onrender.com/docs

---

## 📡 API Endpoint

### POST `/predict`

#### Request Body

```json
{
  "text": "Win a free lottery now!"
}
```

#### Response

```json
{
  "prediction": 1,
  "label": "spam"
}
```

---

##  Machine Learning Workflow

1. Text preprocessing
2. TF-IDF vectorization
3. Logistic Regression model training
4. Model serialization using Pickle
5. API deployment using FastAPI

---

##  Run Locally

### Install dependencies

```bash
pip install -r requirements.txt
```

### Start server

```bash
uvicorn app:app --reload
```

---

##  Author

T S LOKESH
