from NavFooter import NavBar, footer
import streamlit as st

# Page configuration
st.set_page_config(
    page_title="About - Hybrid Text Summarizer",
    layout="wide",
    initial_sidebar_state="collapsed"
)

NavBar()

# Custom CSS for centering and styling
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
        margin-top: 2rem;
        font-size: 2rem;
    }
    .centered-text p, .centered-text ul {
        font-size: 1.3rem;
        text-align: left;
        display: inline-block;
        margin: auto;
    }
    .centered-text ul {
        margin-bottom: 1.5rem;
    }
    </style>
""", unsafe_allow_html=True)

# 📝 About Hybrid Text Summarizer
st.markdown("""
<div class="centered-text">
    <h2>📝 About Hybrid Text Summarizer</h2>
    <p>
        Hybrid Text Summarizer is an AI-powered platform designed to help users quickly condense long articles, reports, or documents into concise, meaningful summaries.
        By combining both extractive and abstractive summarization techniques, this tool provides high-quality, human-like summaries for a wide range of text sources.
    </p>
</div>
""", unsafe_allow_html=True)

# 🎯 Project Purpose
st.markdown("""
<div class="centered-text">
    <h2>🎯 Project Purpose</h2>
    <p>
        In today's information-rich world, people often struggle to process and understand large volumes of text. Hybrid Text Summarizer aims to:
    </p>
    <ul>
        <li>Reduce reading time by generating concise summaries of lengthy documents.</li>
        <li>Assist students, researchers, journalists, and professionals in extracting key information efficiently.</li>
        <li>Support multiple input formats, including plain text, PDF, and Word documents.</li>
        <li>Deliver summaries that combine the accuracy of extractive methods with the fluency of abstractive models.</li>
    </ul>
</div>
""", unsafe_allow_html=True)

# 🛠️ Technologies Used
st.markdown("""
<div class="centered-text">
    <h2>🛠️ Technologies Used</h2>
    <p>
        Hybrid Text Summarizer leverages several advanced technologies:
    </p>
    <ul>
        <li><strong>BERT Extractive Summarizer:</strong> Identifies and selects the most important sentences from the source text using transformer-based models.</li>
        <li><strong>T5 Abstractive Summarizer:</strong> Generates human-like summaries by paraphrasing and condensing extracted content.</li>
        <li><strong>Streamlit:</strong> Provides an intuitive and interactive web interface for users to upload documents and view results.</li>
        <li><strong>Python Libraries:</strong> Utilizes Hugging Face Transformers, PyPDF2, python-docx, and other open-source tools for text processing and model deployment.</li>
    </ul>
</div>
""", unsafe_allow_html=True)

# 🌍 Impact and Applications
st.markdown("""
<div class="centered-text">
    <h2>🌍 Impact and Applications</h2>
    <p>
        By making summarization accessible and efficient, Hybrid Text Summarizer can:
    </p>
    <ul>
        <li>Empower users to make informed decisions faster by focusing on the most relevant information.</li>
        <li>Enhance productivity for professionals who deal with large volumes of text daily.</li>
        <li>Support educational and research activities by simplifying literature reviews and document analysis.</li>
        <li>Enable integration with other applications via its modular and open-source design.</li>
    </ul>
</div>
""", unsafe_allow_html=True)

footer()
