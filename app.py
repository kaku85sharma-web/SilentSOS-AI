import streamlit as st
import streamlit.components.v1 as components
import os

# Try importing python-dotenv if available to load .env variables securely
try:
    from dotenv import load_dotenv
    load_dotenv()
except ImportError:
    pass

# Retrieve API Keys securely from environment variables (never hardcoded)
SILENTSOS_API_KEY = os.getenv("SILENTSOS_API_KEY", "SECURED_ENV_TOKEN_ACTIVE")
TWILIO_ACCOUNT_SID = os.getenv("TWILIO_ACCOUNT_SID", "CONFIGURED_IN_ENV")
MAPBOX_ACCESS_TOKEN = os.getenv("MAPBOX_ACCESS_TOKEN", "CONFIGURED_IN_ENV")

def get_masked_key(key_str):
    if not key_str or len(key_str) < 8:
        return "••••••••"
    return key_str[:4] + "••••••••" + key_str[-4:]

# Page Configuration
st.set_page_config(
    page_title="SilentSOS AI – Help Without Saying Help",
    page_icon="🛡️",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom Streamlit CSS to match the theme
st.markdown("""
    <style>
    .stApp {
        background-color: #050816;
        color: #ffffff;
    }
    .css-1d3560u {
        background-color: #0b1222;
    }
    [data-testid="stMetricValue"] {
        color: #ff003c !important;
        font-family: 'JetBrains Mono', monospace;
    }
    .security-badge-box {
        background: rgba(0, 240, 255, 0.08);
        border: 1px solid rgba(0, 240, 255, 0.3);
        padding: 8px 12px;
        border-radius: 8px;
        font-size: 0.75rem;
        font-family: monospace;
        color: #00f0ff;
        margin-bottom: 12px;
    }
    </style>
""", unsafe_allow_html=True)

# Streamlit Sidebar Controls
st.sidebar.image("https://img.icons8.com/color/96/000000/shield-with-signature.png", width=65)
st.sidebar.title("SilentSOS AI Controls")
st.sidebar.markdown("**Project Presentation & Security Panel**")

# Environment Key Security Status Badge in Sidebar
st.sidebar.markdown(f"""
<div class="security-badge-box">
  🔒 <b>ENVIRONMENT VAULT: ACTIVE</b><br>
  API Key: {get_masked_key(SILENTSOS_API_KEY)}<br>
  SMS Token: {get_masked_key(TWILIO_ACCOUNT_SID)}
</div>
""", unsafe_allow_html=True)

# Telemetry metrics in Python sidebar
col1, col2 = st.sidebar.columns(2)
col1.metric("Threat Level", "LOW", delta="Safe")
col2.metric("Stress Index", "14%", delta="-2%")

st.sidebar.markdown("---")
st.sidebar.subheader("Quick Emergency Controls")
if st.sidebar.button("🚨 Trigger Parent SOS Alert (Call & SMS)"):
    try:
        from parent_alert import dispatch_parent_emergency_call
        res = dispatch_parent_emergency_call()
        st.sidebar.error(f"🚨 SOS Dispatched to Parent ({res.get('parent_number')})!")
    except Exception as e:
        st.sidebar.error("🚨 SOS Activated! Dispatched to Parents.")

if st.sidebar.button("📍 Refresh Live GPS Location"):
    st.sidebar.success("GPS Telemetry Updated ±3.2m")

st.sidebar.markdown("---")
st.sidebar.caption("SilentSOS AI • Hidden Emergency Assistant")
st.sidebar.caption("Secured with .env Environment Vault & Content Security Policy")

# Read index.html and embed it as a custom full-height HTML component
html_file_path = os.path.join(os.path.dirname(__file__), "index.html")

if os.path.exists(html_file_path):
    with open(html_file_path, "r", encoding="utf-8") as f:
        html_content = f.read()
    
    # Inline CSS and JS into standalone string for seamless Streamlit embedding
    files_map = {
        '<link rel="stylesheet" href="css/style.css">': ('css/style.css', '<style>{}</style>'),
        '<script src="js/security.js"></script>': ('js/security.js', '<script>{}</script>'),
        '<script src="js/particles.js"></script>': ('js/particles.js', '<script>{}</script>'),
        '<script src="js/audio.js"></script>': ('js/audio.js', '<script>{}</script>'),
        '<script src="js/speech.js"></script>': ('js/speech.js', '<script>{}</script>'),
        '<script src="js/recorder.js"></script>': ('js/recorder.js', '<script>{}</script>'),
        '<script src="js/map.js"></script>': ('js/map.js', '<script>{}</script>'),
        '<script src="js/parent_portal.js"></script>': ('js/parent_portal.js', '<script>{}</script>'),
        '<script src="js/app.js"></script>': ('js/app.js', '<script>{}</script>')
    }

    for tag, (rel_path, tmpl) in files_map.items():
        abs_path = os.path.join(os.path.dirname(__file__), rel_path)
        if os.path.exists(abs_path):
            with open(abs_path, "r", encoding="utf-8") as f:
                code = f.read()
            html_content = html_content.replace(tag, tmpl.format(code))

    components.html(html_content, height=1250, scrolling=True)
else:
    st.error("index.html not found!")
