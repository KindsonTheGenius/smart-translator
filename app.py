# app.py

import streamlit as st
import requests

OLLAMA_URL = "http://localhost:11434/api/generate"
MODEL_NAME = "mistral"  # Change this to your preferred model name

st.title("🇬🇧 ➡️ 🇫🇷 English to French Translator")
st.write("Powered by a local LLM using [Ollama](https://ollama.com)")

text_to_translate = st.text_area("Enter English text:", height=150)

if st.button("Translate"):
    if not text_to_translate.strip():
        st.warning("Please enter some text to translate.")
    else:
        prompt = f"Translate the following English text to French:\n\n{text_to_translate.strip()}"

        payload = {
            "model": MODEL_NAME,
            "prompt": prompt,
            "stream": False
        }

        try:
            response = requests.post(OLLAMA_URL, json=payload)
            response.raise_for_status()
            result = response.json()["response"].strip()
            st.success("Translation:")
            st.write(result)
        except requests.exceptions.RequestException as e:
            st.error(f"Error communicating with Ollama: {e}")
