# app.py

import streamlit as st
import requests
import base64

# Set page config
st.set_page_config(page_title="English to French Translator", page_icon="🌍", layout="centered")

# Custom CSS for styling
st.markdown("""
    <style>
    .main {
        background-color: #f5f7fa;
    }
    .title {
        font-size: 3rem;
        font-weight: 600;
        color: #2c3e50;
        text-align: center;
        margin-bottom: 1rem;
    }
    .subtitle {
        font-size: 1.2rem;
        color: #34495e;
        text-align: center;
        margin-bottom: 2rem;
    }
    .result-box {
        background-color: #ecf0f1;
        border-radius: 10px;
        padding: 1rem;
        font-size: 1.1rem;
        color: #2c3e50;
    }
    .stButton>button {
        background-color: #3498db;
        color: white;
        font-weight: bold;
        border-radius: 8px;
        padding: 0.5rem 1rem;
        font-size: 1rem;
        transition: 0.3s;
    }
    .stButton>button:hover {
        background-color: #2980b9;
    }
    </style>
""", unsafe_allow_html=True)

# Title and description
st.markdown('<div class="title">🇬🇧 English to 🇫🇷 French Translator</div>', unsafe_allow_html=True)
st.markdown('<div class="subtitle">Powered by your local Ollama LLM</div>', unsafe_allow_html=True)

# Sidebar for model selection (optional)
with st.sidebar:
    st.header("⚙️ Settings")
    model_name = st.selectbox("Select LLM Model", ["mistral", "llama2", "gemma"], index=0)
    st.markdown("Make sure this model is available in your Ollama setup.")

# Input text area
text_to_translate = st.text_area("✏️ Enter English text to translate:", height=150)

# Translate button
if st.button("🌐 Translate"):
    if not text_to_translate.strip():
        st.warning("Please enter some text to translate.")
    else:
        with st.spinner("Translating..."):
            prompt = f"Translate the following English text to French:\n\n{text_to_translate.strip()}"
            payload = {
                "model": model_name,
                "prompt": prompt,
                "stream": False
            }

            try:
                response = requests.post("http://localhost:11434/api/generate", json=payload)
                response.raise_for_status()
                result = response.json()["response"].strip()

                st.markdown("#### 📘 Translated French Text")
                st.markdown(f'<div class="result-box">{result}</div>', unsafe_allow_html=True)

            except requests.exceptions.RequestException as e:
                st.error(f"❌ Error communicating with Ollama: {e}")
