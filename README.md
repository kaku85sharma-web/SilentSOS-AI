# SilentSOS AI – Help Without Saying Help 🛡️

A futuristic, cyber-security AI emergency assistant dashboard built with a dark theme (#050816), glowing neon red accents (#ff003c), smooth glassmorphism, responsive grid layout, and real-time audio visualizers.

---

## 🔒 Security & Environment API Key Management

SilentSOS AI strictly enforces environment key security and zero-hardcoded credentials:

1. **Environment Template (`.env.example`)**:
   - Store all secret API keys (`SILENTSOS_API_KEY`, `TWILIO_ACCOUNT_SID`, `MAPBOX_ACCESS_TOKEN`, `OPENAI_API_KEY`) in `.env`.
   - Copy `.env.example` to `.env` before running in production.

2. **Git Security (`.gitignore`)**:
   - Excludes `.env`, secret tokens, certificate keys, and logs from Git commits.

3. **In-Browser Encrypted Key Vault (`🔒 Key Vault`)**:
   - The UI features a Key Vault modal accessible via the top navigation bar.
   - Credentials saved in the Key Vault are stored in browser session memory with auto-masking (`sk_live_••••••••••••3F9A`).

4. **Contact Phone Number Security**:
   - Toggleable phone number security masking (`+1 (555) ***-9102`) on contact cards.

5. **Security Headers**:
   - HTML includes Content Security & Referrer policy meta tags.

---

## 🌟 Dashboard Features

- **Voice Trigger Panel**: Pulsing mic button, live waveform visualizer canvas, decibel level meter (`dB`), live transcript feed, and optional Hardware Mic FFT analyzer.
- **Safe Phrase Setup**: Add and manage custom secret emergency phrases with phrase test simulation (`⚡ Test`).
- **Emergency Contacts**: Responsive contact cards with avatars, relation tags, and priority labels.
- **Live Location Preview**: Dark cyber map canvas with radar scanner sweep, red pin marker, zoom controls (`+`/`-`), and vector/satellite view mode toggle.
- **Emergency Actions**: Send SOS, Share Location, Start Hidden Recording (timer), and Alert Contacts (stealth SMS).
- **Activity Timeline**: Real-time chronological audit event log.
- **AI Telemetry Sidebar**: Threat Level meter (`LOW`, `MED`, `HIGH`, `CRIT` states altering UI glow colors), Voice Stress Score, and device status telemetry.
- **Covert Calculator Disguise**: Switch interface into a working calculator to prevent discovery. Enter secret code `911=` to return to the SilentSOS dashboard.

---

## 🚀 How to Run

### Direct Browser Launch (Recommended)
```bash
python -m http.server 8000
```
Open `http://localhost:8000`.

### Streamlit Presentation Mode
```bash
pip install streamlit python-dotenv
streamlit run app.py
```
