import streamlit as st
from NavFooter import NavBar, footer

# Page configuration
st.set_page_config(
    page_title="Contact Us - DeepDigest",
    layout="wide",
    initial_sidebar_state="collapsed"
)

NavBar()

# Custom CSS for styling
st.markdown("""
    <style>
    .contact-form {
        max-width: 600px;
        padding: 2rem;
        border-radius: 10px;
        box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
    }
    .contact-form h2 {
        text-align: center;
        margin-bottom: 1.5rem;
    }
    .contact-form label {
        font-weight: 600;
        margin-bottom: 0.5rem;
        display: block;
    }
    .contact-form input[type="text"],
    .contact-form input[type="email"],
    .contact-form textarea {
        width: 100%;
        padding: 0.75rem;
        margin-bottom: 1rem;
        border: 1px solid #ccc;
        border-radius: 5px;
        font-size: 1rem;
    }
    .contact-form button {
        background-color: #4CAF50;
        color: white;
        padding: 0.75rem 1.5rem;
        border: none;
        border-radius: 5px;
        font-size: 1rem;
        cursor: pointer;
        display: block;
        margin: 0 auto;
    }
    .contact-form button:hover {
        background-color: #45a049;
    }
    @media (max-width: 600px) {
        .contact-form {
            padding: 1rem;
        }
    }
    </style>
""", unsafe_allow_html=True)

# Contact Us Form
st.markdown('<div class="contact-form">', unsafe_allow_html=True)
st.markdown('<h2 style="text-align:center;">📬 Contact Us</h2>', unsafe_allow_html=True)

with st.form("contact_form", clear_on_submit=True, border=False):
    name = st.text_input("Name")
    email = st.text_input("Email")
    subject = st.text_input("Subject")
    message = st.text_area("Message", height=150)
    col1, col2, col3 = st.columns([7, 3, 6])
    with col2:
        submitted = st.form_submit_button("Send Message")

    if submitted:
        if name and email and subject and message:
            # Here you could add logic to send an email or store the message
            st.success("Thank you for your message! We'll get back to you shortly.")
        else:
            st.error("Please fill out all fields before submitting.")

st.markdown('</div>', unsafe_allow_html=True)

footer()
