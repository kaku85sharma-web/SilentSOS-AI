import streamlit as st
from datetime import datetime

# ---------------- PAGE CONFIG ----------------
st.set_page_config(
    page_title="SilentSOS AI",
    page_icon="🛡️",
    layout="centered"
)

# ---------------- SIMPLE CSS ----------------
st.markdown(
    """
    <style>
    .stApp {
        background-color: #f5f7fb;
        font-family: Arial, sans-serif;
    }

    .main-box {
        background: white;
        padding: 30px;
        border-radius: 20px;
        box-shadow: 0 4px 12px rgba(0,0,0,0.08);
        text-align: center;
        margin-top: 20px;
    }

    .title {
        color: #111827;
        font-size: 2.2rem;
        font-weight: bold;
    }

    .subtitle {
        color: #4b5563;
        font-size: 1rem;
        margin-bottom: 20px;
    }

    .footer {
        text-align: center;
        color: #6b7280;
        font-size: 0.85rem;
        margin-top: 20px;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# ---------------- HEADER ----------------
st.markdown("<div class='main-box'>", unsafe_allow_html=True)

st.markdown("<div class='title'>🛡️ SilentSOS AI</div>", unsafe_allow_html=True)
st.markdown(
    "<div class='subtitle'>Help Without Saying Help</div>",
    unsafe_allow_html=True
)

st.write(
    "If you feel unsafe, press the emergency button below. "
    "The app will notify your trusted contact."
)

st.markdown("---")

# ---------------- USER INFO ----------------
name = st.text_input("Your Name", placeholder="Enter your name")
phone = st.text_input("Emergency Contact Number", placeholder="+91XXXXXXXXXX")

st.markdown("---")

# ---------------- BUTTONS ----------------
if st.button("🚨 Send Emergency Alert", use_container_width=True):
    time_now = datetime.now().strftime("%d-%m-%Y %I:%M %p")

    st.error("🚨 Emergency Alert Sent!")

    st.write(f"**Name:** {name if name else 'User'}")
    st.write(f"**Emergency Contact:** {phone if phone else 'Not provided'}")
    st.write(f"**Time:** {time_now}")

    st.success("Your trusted contact has been notified successfully.")

if st.button("📍 Share My Location", use_container_width=True):
    st.success("📍 Location shared successfully.")
    st.info("Demo Location: Najafgarh, Delhi, India")

if st.button("✅ I Am Safe", use_container_width=True):
    st.success("Status updated: You are marked safe.")

st.markdown("---")

# ---------------- SAFETY TIPS ----------------
st.subheader("Quick Safety Tips")
st.markdown(
    """
- Stay in a public place if possible.
- Call a trusted person immediately.
- Share your live location with family.
- Keep your phone charged.
- In a real emergency, contact local emergency services.
"""
)

st.markdown("</div>", unsafe_allow_html=True)

# ---------------- FOOTER ----------------
st.markdown(
    "<div class='footer'>SilentSOS AI • Simple Emergency Assistant • Demo Project</div>",
    unsafe_allow_html=True
)
