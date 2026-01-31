import streamlit as st
import numpy as np
from PIL import Image

st.set_page_config(page_title="Plant Disease Detection Chatbot", page_icon="🌱")

st.title("🌿 Plant Disease Detection Chatbot")

if "chat" not in st.session_state:
    st.session_state.chat = []

def detect_from_text(text):
    text = text.lower()

    if "yellow" in text:
        return "Chlorosis", [
            "Ensure proper sunlight",
            "Avoid overwatering",
            "Apply nitrogen fertilizer"
        ]
    elif "brown spots" in text:
        return "Leaf Spot Disease", [
            "Remove infected leaves",
            "Use neem oil spray",
            "Avoid water on leaves"
        ]
    else:
        return "Unknown Disease", [
            "Upload a clear leaf image",
            "Consult agriculture expert"
        ]

def detect_from_image(image):
    img = np.array(image)
    mean_val = np.mean(img)

    if mean_val < 120:
        return "Possible Fungal Infection", [
            "Apply fungicide",
            "Improve air circulation"
        ]
    else:
        return "Healthy Plant", [
            "Continue regular care"
        ]

text = st.text_input("Type plant symptoms")

if text:
    disease, steps = detect_from_text(text)
    st.session_state.chat.append(("Farmer", text))
    reply = f"Disease: {disease}\n"
    for i, s in enumerate(steps, 1):
        reply += f"{i}. {s}\n"
    st.session_state.chat.append(("Bot", reply))

image_file = st.file_uploader("Upload leaf image", type=["jpg", "png"])

if image_file:
    image = Image.open(image_file)
    st.image(image)
    disease, steps = detect_from_image(image)
    reply = f"Disease: {disease}\n"
    for i, s in enumerate(steps, 1):
        reply += f"{i}. {s}\n"
    st.session_state.chat.append(("Bot", reply))

for sender, msg in st.session_state.chat:
    st.markdown(f"**{sender}:** {msg}")
