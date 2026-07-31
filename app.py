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

    /* Main page */
    .stApp {
        background-color: #f5f7fb;
        color: #111827;
    }

    /* Remove dark Streamlit header */
    header[data-testid="stHeader"] {
        background: transparent;
    }

    div[data-testid="stToolbar"] {
        right: 1rem;
    }

    /* Make all text dark */
    h1, h2, h3, h4, h5, h6, p, div, span, label {
        color: #111827 !important;
    }

    /* Header */
    .logo-title {
        font-size: 2.3rem;
        font-weight: 800;
        color: #111827;
    }

    .logo-red {
        color: #ef4444;
    }

    .subtitle {
        color: #6b7280 !important;
        margin-top: -6px;
    }

    .status-pill {
        background: #ecfdf5;
        color: #047857 !important;
        padding: 10px 18px;
        border-radius: 999px;
        font-weight: 700;
        border: 1px solid #bbf7d0;
        display: inline-block;
        text-align: center;
    }

    /* Hero card */
    .hero-card {
        background: white;
        border: 1px solid #f0d6d6;
        border-radius: 28px;
        padding: 3rem 2rem;
        text-align: center;
        box-shadow: 0 10px 24px rgba(0,0,0,0.05);
    }

    .hero-title {
        font-size: 3rem;
        font-weight: 800;
        margin-bottom: 0.5rem;
    }

    .hero-text {
        font-size: 1.1rem;
        color: #4b5563 !important;
        max-width: 700px;
        margin: auto;
    }

    /* Big SOS button */
    .sos-button button {
        background: linear-gradient(90deg, #ef4444, #ff4d4f) !important;
        color: white !important;
        font-size: 1.2rem !important;
        font-weight: 800 !important;
        border-radius: 18px !important;
        height: 70px !important;
        width: 100% !important;
        border: none !important;
        box-shadow: 0 8px 20px rgba(239,68,68,0.25);
    }

    /* Feature cards */
    .feature-card {
        background: white;
        border: 1px solid #e8edf5;
        border-radius: 24px;
        padding: 2rem 1.5rem;
        text-align: center;
        box-shadow: 0 4px 14px rgba(0,0,0,0.04);
        min-height: 300px;
    }

    .feature-card h3 {
        margin-top: 0.5rem;
        margin-bottom: 0.5rem;
    }

    .feature-card p {
        color: #4b5563 !important;
        font-size: 0.98rem;
    }

    /* Colored buttons */
    .blue-btn button {
        background: #2563eb !important;
        color: white !important;
        border-radius: 14px !important;
        width: 100%;
        font-weight: 700;
    }

    .green-btn button {
        background: #16a34a !important;
        color: white !important;
        border-radius: 14px !important;
        width: 100%;
        font-weight: 700;
    }

    .purple-btn button {
        background: #7c3aed !important;
        color: white !important;
        border-radius: 14px !important;
        width: 100%;
        font-weight: 700;
    }

    /* Steps */
    .step-card {
        background: white;
        border: 1px solid #e8edf5;
        border-radius: 20px;
        padding: 1.5rem 1rem;
        text-align: center;
        box-shadow: 0 2px 10px rgba(0,0,0,0.03);
        min-height: 220px;
    }

    .step-card p {
        color: #4b5563 !important;
    }

    /* Safety box */
    .safety-box {
        background: #f8fbff;
        border: 1px solid #dbeafe;
        border-radius: 18px;
        padding: 1.5rem;
    }

    /* Footer */
    .footer-box {
        background: white;
        border: 1px solid #e8edf5;
        border-radius: 18px;
        padding: 1.5rem;
        text-align: center;
        color: #6b7280 !important;
        box-shadow: 0 2px 10px rgba(0,0,0,0.03);
    }

    </style>
    """,
    unsafe_allow_html=True
)

# ---------------- HEADER ----------------
c1, c2 = st.columns([4, 1])

with c1:
    st.markdown(
        """
        <div class="logo-title">
            🛡️ Silent<span class="logo-red">SOS</span> AI
        </div>
        <div class="subtitle">Help Without Saying Help</div>
        """,
        unsafe_allow_html=True
    )

with c2:
    st.markdown(
        '<div class="status-pill">🟢 System Ready</div>',
        unsafe_allow_html=True
    )

st.markdown("<br>", unsafe_allow_html=True)

# ---------------- HERO SECTION ----------------
st.markdown('<div class="hero-card">', unsafe_allow_html=True)

st.markdown('<div style="font-size:4.5rem;">🛡️</div>', unsafe_allow_html=True)

st.markdown(
    '<div class="hero-title">Need Help?</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="hero-text">Press the button below to send an emergency alert to your trusted contacts instantly.</div>',
    unsafe_allow_html=True
)

st.markdown("<br>", unsafe_allow_html=True)

st.markdown('<div class="sos-button">', unsafe_allow_html=True)
if st.button("🚨 SEND EMERGENCY ALERT"):
    now = datetime.now().strftime("%d %b %Y • %I:%M %p")
    st.error("🚨 Emergency Alert Sent Successfully!")
    st.success(f"Alert Time: {now}")
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
    st.markdown(
        '<p>Share your current location with your trusted contacts instantly.</p>',
        unsafe_allow_html=True
    )
    st.markdown('<div class="blue-btn">', unsafe_allow_html=True)
    if st.button("📍 SHARE LOCATION"):
        st.success("Location shared successfully!")
    st.markdown("</div>", unsafe_allow_html=True)
    st.markdown("</div>", unsafe_allow_html=True)

with col2:
    st.markdown('<div class="feature-card">', unsafe_allow_html=True)
    st.markdown('<div style="font-size:3rem;">✅</div>', unsafe_allow_html=True)
    st.markdown("### I Am Safe")
    st.markdown(
        '<p>Inform your contacts that you are safe now and no help is needed.</p>',
        unsafe_allow_html=True
    )
    st.markdown('<div class="green-btn">', unsafe_allow_html=True)
    if st.button("✅ I AM SAFE"):
        st.success("Status updated: You are safe.")
    st.markdown("</div>", unsafe_allow_html=True)
    st.markdown("</div>", unsafe_allow_html=True)

with col3:
    st.markdown('<div class="feature-card">', unsafe_allow_html=True)
    st.markdown('<div style="font-size:3rem;">👥</div>', unsafe_allow_html=True)
    st.markdown("### My Contacts")
    st.markdown(
        '<p>View and manage your trusted emergency contacts easily.</p>',
        unsafe_allow_html=True
    )
    st.markdown('<div class="purple-btn">', unsafe_allow_html=True)
    if st.button("👥 VIEW CONTACTS"):
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

t1, t2, t3 = st.columns(3)

with t1:
    st.markdown("✅ Stay calm and move to a safe place")

with t2:
    st.markdown("📍 Share location with trusted people")

with t3:
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
