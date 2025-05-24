import streamlit as st
import os
from PIL import Image
from Hybrid_summarizer.model_loader import load_abstracter
from Hybrid_summarizer.hybrid_summarizer import hybrid_summarize
from NavFooter import NavBar, footer
import PyPDF2
import docx

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
    "summ": "assets/summerization.jpg"
}
images, missing = load_images(image_paths)
for path in missing:
    st.warning(f"Image not found: {path}")

NavBar()

if "summ" in images:
    st.image(images["summ"], use_container_width=True, output_format="PNG", caption=None)

st.markdown("<h2 style='text-align: center;'>Select the Format</h2>", unsafe_allow_html=True)
st.markdown("<br><br>", unsafe_allow_html=True)

# --- Load models at the very start (cached) ---
@st.cache_resource
def get_models():
    abstracter, tokenizer = load_abstracter("models/t5_abstracter")
    return abstracter, tokenizer

abstracter, tokenizer = get_models()

# --- Session state for workflow management ---
if 'selected_opt' not in st.session_state:
    st.session_state.selected_opt = None
if 'uploaded_text' not in st.session_state:
    st.session_state.uploaded_text = ""
if 'text_done' not in st.session_state:
    st.session_state.text_done = False
if 'summary' not in st.session_state:
    st.session_state.summary = ""
if 'file_error' not in st.session_state:
    st.session_state.file_error = ""

# --- Option selection row ---
col1, col2, col3 = st.columns(3)
with col1:
    text_opt = st.button("Text")
with col2:
    pdf_opt = st.button("PDF")
with col3:
    word_opt = st.button("Word")

if text_opt:
    st.session_state.selected_opt = "text"
    st.session_state.text_done = False
    st.session_state.uploaded_text = ""
    st.session_state.summary = ""
    st.session_state.file_error = ""
if pdf_opt:
    st.session_state.selected_opt = "pdf"
    st.session_state.text_done = False
    st.session_state.uploaded_text = ""
    st.session_state.summary = ""
    st.session_state.file_error = ""
if word_opt:
    st.session_state.selected_opt = "word"
    st.session_state.text_done = False
    st.session_state.uploaded_text = ""
    st.session_state.summary = ""
    st.session_state.file_error = ""

# --- INPUT HANDLING ---
if st.session_state.selected_opt == "text":
    if not st.session_state.text_done:
        text_input = st.text_area("Paste your text here for summarization", value=st.session_state.uploaded_text, height=250)
        if st.button("Done"):
            st.session_state.uploaded_text = text_input.strip()
            st.session_state.text_done = True
            st.session_state.summary = ""
    else:
        st.info("Text input locked. Click Summarize to continue or Reset to start over.")

elif st.session_state.selected_opt in ["pdf", "word"]:
    file_types = ["pdf"] if st.session_state.selected_opt == "pdf" else ["docx"]
    uploaded_file = st.file_uploader(f"Upload your {st.session_state.selected_opt.upper()} file (max 2MB)", type=file_types)
    if uploaded_file:
        if uploaded_file.size > 2 * 1024 * 1024:
            st.session_state.file_error = "File size exceeds 2MB limit!"
        else:
            try:
                if st.session_state.selected_opt == "pdf":
                    reader = PyPDF2.PdfReader(uploaded_file)
                    text = ""
                    for page in reader.pages:
                        page_text = page.extract_text()
                        if page_text:
                            text += page_text + "\n"
                    st.session_state.uploaded_text = text.strip()
                elif st.session_state.selected_opt == "word":
                    doc = docx.Document(uploaded_file)
                    text = "\n".join([para.text for para in doc.paragraphs if para.text.strip()])
                    st.session_state.uploaded_text = text.strip()
                st.session_state.text_done = True
                st.session_state.summary = ""
                st.session_state.file_error = ""
            except Exception as e:
                st.session_state.file_error = f"Could not read file: {e}"

if st.session_state.file_error:
    st.error(st.session_state.file_error)

# --- SUMMARIZATION ---
if st.session_state.text_done and st.session_state.uploaded_text and not st.session_state.file_error:
    if st.session_state.summary == "":
        if st.button("Summarize"):
            with st.spinner("Summarizing..."):
                summary = hybrid_summarize(
                    st.session_state.uploaded_text,
                    abstracter=abstracter,
                    tokenizer=tokenizer,
                    num_sentences=5,
                    max_abstractive_tokens=128,
                    desired_word_count=60,
                    chunk_words=400,
                    chunk_overlap=50
                )
            st.session_state.summary = summary
    if st.session_state.summary:
        st.success("Done!")
        st.text_area("Summary Output", st.session_state.summary, height=200)
        # --- Reset Button (only after summarization is done) ---
        if st.button("Reset"):
            for key in ['selected_opt', 'uploaded_text', 'text_done', 'summary', 'file_error']:
                st.session_state[key] = None if key == 'selected_opt' else ""
            st.rerun()
else:
    if st.session_state.selected_opt and not st.session_state.file_error and not st.session_state.text_done:
        st.info("Please enter or upload text, then click Done.")

# --- Optional: CSS for full-width buttons ---
st.markdown("""
<style>
    .stButton>button { width: 100%; }
</style>
""", unsafe_allow_html=True)

footer()
