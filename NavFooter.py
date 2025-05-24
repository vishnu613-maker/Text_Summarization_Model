import streamlit as st
import os

def NavBar():
    # Load external CSS for styling
    css_file_path = os.path.join("assets", "css", "style.css")
    with open(css_file_path) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

    # Use st.columns with small gap and tight widths (no HTML wrapper)
    cols = st.columns([5, 1, 1.5, 1, 1], gap="small")

    with cols[0]:
        st.markdown(
            '<h1 class="project-title" style="margin-bottom: 0;">📄DeepDigest</h1>',
            unsafe_allow_html=True,
        )
    with cols[1]:
        st.page_link("app.py", label="Home")
    with cols[2]:
        st.page_link("pages/summarizer.py", label="Summarize text")
    with cols[3]:
        st.page_link("pages/about.py", label="About")
    with cols[4]:
        st.page_link("pages/contactus.py", label="Contact Us")

    # Add a spacer for the fixed navbar, if you have fixed positioning in your CSS
    st.markdown("<div style='margin-bottom: 0%;'></div>", unsafe_allow_html=True)


def footer():
    st.markdown("""
        <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css">
        <style>
        html, body {
            margin: 0;
            padding: 0;
        }
        .fa-brands {
            font-size: xx-large !important;
            margin: 0 10px;
        }
        .footer {
            background-color: #333333;
            color: white;
            padding: 40px 0 10px 0;
            border-top-left-radius: 25px;
            border-top-right-radius: 25px;
            margin-top: 10% !important;
        }
        .footer a {
            color: #ffffff;
            text-decoration: none;
        }
        .footer a:hover {
            text-decoration: underline;
        }
        </style>
        <div class="footer">
            <div style="display: flex; justify-content: center;">
                <i class="fa-brands fa-facebook"></i>
                <i class="fa-brands fa-instagram"></i>
                <i class="fa-brands fa-twitter"></i>
                <i class="fa-brands fa-youtube"></i>
            </div>
            <br>
            <div style="display: flex; justify-content: center; flex-wrap: wrap; gap: 20px;">
                <h6>About DeepDigest</h6>
                <h6>Privacy Policy</h6>
                <h6>Terms of Service</h6>
            </div>
            <p style="margin-top: 10px; text-align:center;">© 2025 DeepDigest. All rights reserved.</p>
        </div>
    """, unsafe_allow_html=True)
