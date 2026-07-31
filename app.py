import streamlit as st
from datetime import datetime

# ---------------- PAGE CONFIG ----------------
st.set_page_config(
    page_title="SilentSOS AI",
    page_icon="🛡️",
    layout="wide"
)

# ---------------- CUSTOM CSS ----------------
st.markdown(
    """
    <style>
    .stApp {
        background-color: #f5f7fb;
    }

    .main-card {
        background: white;
        padding: 2rem;
        border-radius: 24px;
        border: 1px solid #f0d6d6;
        box-shadow: 0 8px 24px rgba(0,0,0,0.05);
        text-align: center;
    }

    .feature-card {
        background: white;
        padding: 1.5rem;
        border-radius: 22px;
        border: 1px solid #e8edf5;
        box-shadow: 0 4px 14px rgba(0,0,0,0.04);
        text-align: center;
        min-height: 260px;
    }

    .step-card {
        background: white;
        padding: 1.2rem;
        border-radius: 18px;
        border: 1px solid #e8edf5;
        text-align: center;
        height: 100%;
    }

    .footer-box {
        background: white;
        border: 1px solid #e8edf5;
        border-radius: 16px;
        padding: 1rem;
        text-align: center;
        color: #6b7280;
    }

    .logo-title {
        font-size: 2.2rem;
        font-weight: 800;
        color: #111827;
    }

    .logo-red {
        color: #ef4444;
    }

    .subtitle {
        color: #6b7280;
        margin-top: -8px;
    }

    .big-heading {
        font-size: 2.8rem;
        font-weight: 800;
        color: #111827;
        margin-bottom: 0.5rem;
    }

    .muted {
        color: #4b5563;
        font-size: 1.05rem;
    }

    .sos-button button {
        background: linear-gradient(90deg, #ef4444, #ff4d4f) !important;
        color: white !important;
        font-size: 1.15rem !important;
        font-weight: 700 !important;
        border-radius: 16px !important;
        height: 3.8rem !important;
        width: 100% !important;
        border: none !important;
    }

    .blue-button button {
        background: #2563eb !important;
        color: white !important;
        border-radius: 12px !important;
        width: 100%;
    }

    .green-button button {
        background: #16a34a !important;
        color: white !important;
        border-radius: 12px !important;
        width: 100%;
    }

    .purple-button button {
        background: #7c3aed !important;
        color: white !important;
        border-radius: 12px !important;
        width: 100%;
    }

    .status-pill {
        background: #ecfdf5;
        color: #047857;
        padding: 0.5rem 1rem;
        border-radius: 999px;
        font-weight: 600;
        border: 1px solid #bbf7d0;
        display: inline-block;
    }

    .safety-box {
        background: #f8fbff;
        border: 1px solid #dbeafe;
        border-radius: 16px;
        padding: 1rem;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# ---------------- HEADER ----------------
header_col1, header_col2 = st.columns([4, 1])

with header_col1:
    st.markdown(
        """
        <div class="logo-title">
            🛡️ Silent<span class="logo-red">SOS</span> AI
        </div>
        <div class="subtitle">Help Without Saying Help</div>
        """,
        unsafe_allow_html=True
    )

with header_col2:
    st.markdown(
        '<div class="status-pill">🟢 System Ready</div>',
        unsafe_allow_html=True
    )

st.markdown("<br>", unsafe_allow_html=True)

# ---------------- HERO CARD ----------------
st.markdown('<div class="main-card">', unsafe_allow_html=True)

st.markdown('<div style="font-size:4rem;">🛡️</div>', unsafe_allow_html=True)
st.markdown('<div class="big-heading">Need Help?</div>', unsafe_allow_html=True)
st.markdown(
    '<div class="muted">Press the button below to send an emergency alert to your trusted contacts.</div>',
    unsafe_allow_html=True
)

st.markdown("<br>", unsafe_allow_html=True)

st.markdown('<div class="sos-button">', unsafe_allow_html=True)
if st.button("🚨 SEND EMERGENCY ALERT", key="sos"):
    now = datetime.now().strftime("%d %b %Y • %I:%M %p")
    st.error("🚨 Emergency Alert Sent Successfully!")
    st.success(f"Alert time: {now}")
    st.info("Your trusted contacts have been notified.")
st.markdown("</div>", unsafe_allow_html=True)

st.markdown("</div>", unsafe_allow_html=True)

st.markdown("<br>", unsafe_allow_html=True)

# ---------------- FEATURE CARDS ----------------
col1, col2, col3 = st.columns(3)

with col1:
    st.markdown('<div class="feature-card">', unsafe_allow_html=True)
    st.markdown('<div style="font-size:3rem;">📍</div>', unsafe_allow_html=True)
    st.markdown("### Share My Location")
    st.write("Share your current location with your trusted contacts instantly.")
    st.markdown('<div class="blue-button">', unsafe_allow_html=True)
    if st.button("📍 SHARE LOCATION", key="loc"):
        st.success("Location shared successfully!")
    st.markdown("</div>", unsafe_allow_html=True)
    st.markdown("</div>", unsafe_allow_html=True)

with col2:
    st.markdown('<div class="feature-card">', unsafe_allow_html=True)
    st.markdown('<div style="font-size:3rem;">✅</div>', unsafe_allow_html=True)
    st.markdown("### I Am Safe")
    st.write("Inform your contacts that you are safe now and no help is needed.")
    st.markdown('<div class="green-button">', unsafe_allow_html=True)
    if st.button("✅ I AM SAFE", key="safe"):
        st.success("Status updated: You are safe.")
    st.markdown("</div>", unsafe_allow_html=True)
    st.markdown("</div>", unsafe_allow_html=True)

with col3:
    st.markdown('<div class="feature-card">', unsafe_allow_html=True)
    st.markdown('<div style="font-size:3rem;">👥</div>', unsafe_allow_html=True)
    st.markdown("### My Contacts")
    st.write("View and manage your trusted emergency contacts easily.")
    st.markdown('<div class="purple-button">', unsafe_allow_html=True)
    if st.button("👥 VIEW CONTACTS", key="contacts"):
        st.info("Trusted Contacts:\\n• Mom\\n• Dad\\n• Sister\\n• Best Friend")
    st.markdown("</div>", unsafe_allow_html=True)
    st.markdown("</div>", unsafe_allow_html=True)

st.markdown("<br>", unsafe_allow_html=True)

# ---------------- HOW IT WORKS ----------------
st.markdown("## How SilentSOS AI Works")

s1, s2, s3, s4 = st.columns(4)

with s1:
    st.markdown(
        '<div class="step-card"><div style="font-size:2rem;">👆</div><h4>1. Press Alert</h4><p>Tap the emergency button when in danger.</p></div>',
        unsafe_allow_html=True
    )

with s2:
    st.markdown(
        '<div class="step-card"><div style="font-size:2rem;">🔔</div><h4>2. Send Alert</h4><p>Alert (SMS + Call) is sent to your contacts.</p></div>',
        unsafe_allow_html=True
    )

with s3:
    st.markdown(
        '<div class="step-card"><div style="font-size:2rem;">📍</div><h4>3. Share Location</h4><p>Your live location is shared instantly.</p></div>',
        unsafe_allow_html=True
    )

with s4:
    st.markdown(
        '<div class="step-card"><div style="font-size:2rem;">🛡️</div><h4>4. Get Help</h4><p>Your contacts can reach you quickly.</p></div>',
        unsafe_allow_html=True
    )

st.markdown("<br>", unsafe_allow_html=True)

# ---------------- SAFETY TIPS ----------------
st.markdown('<div class="safety-box">', unsafe_allow_html=True)
st.markdown("### 🛡️ Safety Tips")

tip1, tip2, tip3 = st.columns(3)

with tip1:
    st.markdown("✅ Stay calm and move to a safe place")

with tip2:
    st.markdown("📍 Share location with trusted people")

with tip3:
    st.markdown("📞 Call local emergency services if needed")

st.markdown("</div>", unsafe_allow_html=True)

st.markdown("<br>", unsafe_allow_html=True)

# ---------------- FOOTER ----------------
st.markdown(
    """
    <div class="footer-box">
        <b>🛡️ SilentSOS AI</b><br>
        Your Safety, Our Priority ❤️<br>
        v1.0.0
    </div>
    """,
    unsafe_allow_html=True
)
