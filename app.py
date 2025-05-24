import streamlit as st
import os
from PIL import Image
from NavFooter import NavBar, footer

# Set page configuration
st.set_page_config(
    page_title="DeepDigest - Text Summarization Model",
    layout="wide",
    initial_sidebar_state="collapsed"
)

@st.cache_data
def load_images(image_paths):
    images = {}
    missing = []
    for key, path in image_paths.items():
        if os.path.exists(path):
            images[key] = Image.open(path)
        else:
            missing.append(path)
    return images, missing

# Define paths to images
image_paths = {
    "text": "assets/text_summarization.png",
    "combo": "assets/combo.png"
    
}
images, missing = load_images(image_paths)
for path in missing:
    st.warning(f"Image not found: {path}")


# Navbar
NavBar()

# Hero Section
if "text" in images:
    st.image(images["text"], use_container_width=True, output_format="PNG", caption=None)



st.markdown("""
    <style>
    .centered-text {
        text-align: center;
        max-width: 900px;
        margin: auto;
        padding: 1rem 1rem;
        line-height: 1.8;
        font-size: 1.3rem;
    }
    .centered-text h2 {
        
        font-size: 2rem;
    }
    .centered-text p, .centered-text ul {
        font-size: 1.3rem;
        text-align: center;
        display: inline-block;
        margin: auto;
    }
    .centered-text ul {
        margin-bottom: 1.5rem;
    }
    </style>
""", unsafe_allow_html=True)
st.markdown("""
<div class="centered-text">
    <h2>A Hybrid Text Summarizer!</h2>
    <p>**Struggling to condense long articles, reports, or documents?**</p>
    <p>You're not alone. Many people waste hours reading, re-reading, and trying to extract the main points from massive walls of text.
    </p>
</div>
""", unsafe_allow_html=True)

if "combo" in images:
    st.image(images["combo"], use_container_width=True, output_format="PNG", caption=None)
    
st.markdown("""
<div class="centered-text">
    <p>This project combines the power of extractive and abstractive AI summarization, letting you instantly generate concise, high-quality summaries from even the longest texts.  
    Whether you're a student, journalist, researcher, or just overwhelmed by information, our tool saves you time and delivers clarity!</p>
</div>
""", unsafe_allow_html=True)

footer()

