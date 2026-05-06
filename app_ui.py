import streamlit as st
import requests

# Page config
st.set_page_config(page_title="Spam Classifier", page_icon="📩")

st.title("📩 Spam Classifier App")
st.write("Enter a message and check whether it is Spam or Not Spam.")

# Input box
text = st.text_area("Enter your message here:")

# Your deployed API URL (Render)
API_URL = "https://spam-classifier-api-3hos.onrender.com/predict"

# Button
if st.button("Predict"):
    if text.strip() == "":
        st.warning("Please enter a message first.")
    else:
        try:
            response = requests.post(API_URL, json={"text": text})

            if response.status_code == 200:
                result = response.json()

                st.subheader("Result")
                st.write("Input:", result["input_text"])
                st.success(f"Prediction: {result['label']}")

            else:
                st.error("API Error: Could not get response")

        except Exception as e:
            st.error(f"Request failed: {e}")