import streamlit as st
import pandas as pd
# Set up page configuration
st.set_page_config(page_title="MEDai - Medical Diagnostics", layout="wide")

# Load data
@st.cache_data
def load_data():
    return pd.read_csv("data/disease.csv")

df = load_data()



# Custom CSS for styling
with open("styles.css") as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

# Navbar
st.markdown("""
<nav class="navbar">
    <div class="nav-left">
        <img src="https://via.placeholder.com/40" class="logo" />
        <span class="title">MEDai</span>
    </div>
    <div class="nav-right">
        <a href="#home">Home</a>
        <a href="#faq">FAQ</a>
        <a href="#about">About Us</a>
        <a href="#contact">Contact</a>
    </div>
</nav>
""", unsafe_allow_html=True)

# Hero Section
st.markdown('<div id="home"></div>', unsafe_allow_html=True)
st.title("MEDai")
st.subheader("Medical diagnostics for everyone")

symptoms_input = st.text_input("Enter your symptoms (comma separated):", key="symptoms")
if st.button("Detect Disease"):
    user_symptoms = set(sym.strip().lower() for sym in symptoms_input.split(","))
    matched = None
    for idx, row in df.iterrows():
        disease_symptoms = set(sym.strip().lower() for sym in row["Symptoms"].split(","))
        if user_symptoms.intersection(disease_symptoms):
            matched = row
            break

    if matched is not None:
        st.success(f"**Possible Disease:** {matched['Name']}")
        st.info(f"**Prevention:** {matched['Prevention']}")
        st.warning(f"**Treatment:** {matched['Treatment']}")
    else:
        st.error("No matching disease found. Please try with more common symptoms.")

# FAQ Section
st.markdown('<div id="faq"></div>', unsafe_allow_html=True)
st.header("Frequently Asked Questions")
faq_data = [
    ("How does MEDai work?", "We use a simple matching algorithm comparing your symptoms with our database."),
    ("Is this a replacement for a doctor?", "No. MEDai is only an assistant tool. Always consult a healthcare provider."),
    ("What kind of diseases can it detect?", "We cover common diseases with general symptoms."),
]
for question, answer in faq_data:
    with st.expander(question):
        st.write(answer)

# About Us Section
st.markdown('<div id="about"></div>', unsafe_allow_html=True)
st.header("About Us")
st.write("""
We at MEDai are committed to helping individuals access basic diagnostic help.  
Our goal is to empower people with better understanding of their health before visiting a doctor.  
MEDai was made with love and care for the betterment of society.
""")

# Contact Section
st.markdown('<div id="contact"></div>', unsafe_allow_html=True)
st.header("Contact Us")
with st.form("contact_form"):
    name = st.text_input("Your Name")
    email = st.text_input("Your Email")
    message = st.text_area("Message")
    submitted = st.form_submit_button("Send")
    if submitted:
        st.success("Thank you! We'll get back to you soon.")

# Footer
st.markdown("""
<footer class="footer">
    <div class="footer-links">
        <a href="#home">Home</a> |
        <a href="#faq">FAQ</a> |
        <a href="#about">About Us</a> |
        <a href="#contact">Contact</a>
    </div>
    <p>© 2025 MEDai. All rights reserved.</p>
</footer>
""", unsafe_allow_html=True)

# Go to top button
st.markdown("""
<a href="#home" class="go-top">⬆️ Go to Top</a>
""", unsafe_allow_html=True)
