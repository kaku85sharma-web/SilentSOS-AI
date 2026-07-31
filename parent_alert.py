"""
SilentSOS AI - Parent Emergency Alert System
"""
import os
import json
import sys

# Safe import with linter directive to eliminate IDE warnings
try:
    from dotenv import load_dotenv  # type: ignore
    load_dotenv()
except Exception:
    pass

try:
    from twilio.rest import Client  # type: ignore
except Exception:
    Client = None

# UTF-8 encoding support for Windows terminal output
if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")

# Retrieve Twilio Credentials from environment
TWILIO_ACCOUNT_SID = os.getenv("TWILIO_ACCOUNT_SID")
TWILIO_AUTH_TOKEN = os.getenv("TWILIO_AUTH_TOKEN")
TWILIO_FROM_NUMBER = os.getenv("TWILIO_FROM_NUMBER")
PARENT_PHONE_NUMBER = os.getenv("PARENT_PHONE_NUMBER", "+15550009102")

def dispatch_parent_emergency_call(parent_number=None, location_url=None):
    """
    Dispatches a real automated voice phone call to the parent/guardian via Twilio API.
    """
    target_phone = parent_number or PARENT_PHONE_NUMBER
    loc_link = location_url or "https://silentsos.ai/track/guardian-live"

    print(f"🚨 Initiating Real Emergency Dispatch to Parent: {target_phone}...")

    if not TWILIO_ACCOUNT_SID or not TWILIO_AUTH_TOKEN or TWILIO_ACCOUNT_SID.startswith("AC_YOUR") or not Client:
        print("⚠️ Twilio API keys not set in .env. Running simulated Parent Voice Call & SMS dispatch.")
        return {
            "status": "simulated",
            "message": f"Simulated call & SMS dispatched to Parent ({target_phone}). Live Location: {loc_link}",
            "parent_number": target_phone,
            "location": loc_link
        }

    try:
        client = Client(TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN)

        # 1. Dispatch Real Automated Emergency Voice Call
        call = client.calls.create(
            twiml=f'''<Response>
                <Say voice="alice">Emergency Alert from SilentSOS AI. Your relative has triggered a covert distress signal. Live location tracking and audio capture have been activated. Please check your text messages immediately for the live tracking link.</Say>
            </Response>''',
            to=target_phone,
            from_=TWILIO_FROM_NUMBER
        )

        # 2. Dispatch Real Emergency SMS with Live Map Tracking Link
        sms = client.messages.create(
            body=f"🚨 EMERGENCY ALERT: SilentSOS AI detected distress. Track live GPS location & listen to covert audio here: {loc_link}",
            to=target_phone,
            from_=TWILIO_FROM_NUMBER
        )

        print(f"✅ Real Emergency Call SID: {call.sid}")
        print(f"✅ Real SMS Message SID: {sms.sid}")

        return {
            "status": "success",
            "call_sid": call.sid,
            "sms_sid": sms.sid,
            "parent_number": target_phone,
            "location": loc_link
        }

    except Exception as e:
        print(f"❌ Twilio Dispatch Error: {e}")
        return {
            "status": "error",
            "error": str(e),
            "parent_number": target_phone
        }

if __name__ == "__main__":
    print("File loaded successfully")
    result = dispatch_parent_emergency_call()
    print(json.dumps(result, indent=2))
