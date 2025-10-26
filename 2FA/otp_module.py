# otp_module.py
import random, time
from email_service import send_email
from config import OTP_EXPIRY
from rsa_utils import load_keys, encrypt_message, decrypt_message

otp_data = {"encrypted_otp": None, "timestamp": None}

def generate_otp():
    return str(random.randint(100000, 999999))

def send_otp_email(user_email):
    otp = generate_otp()
    private_key, public_key = load_keys()
    encrypted_otp = encrypt_message(otp, public_key)
    otp_data["encrypted_otp"] = encrypted_otp
    otp_data["timestamp"] = time.time()
    message = f"Your encrypted OTP is:\n{encrypted_otp}\n\nIt will expire in {OTP_EXPIRY} seconds."
    send_email(user_email, "Your Secure Encrypted OTP", message)
    print("Encrypted OTP sent successfully!")
    return otp

def is_otp_valid(user_otp):
    if not otp_data["encrypted_otp"]:
        return False, "No OTP generated yet."
    private_key, _ = load_keys()
    decrypted_otp = decrypt_message(otp_data["encrypted_otp"], private_key)
    current_time = time.time()
    if current_time - otp_data["timestamp"] > OTP_EXPIRY:
        return False, "OTP expired. Please request a new one."
    if user_otp == decrypted_otp:
        return True, "OTP verified successfully!"
    else:
        return False, "Invalid OTP. Please try again."

def resend_otp(user_email):
    print("Resending encrypted OTP...")
    return send_otp_email(user_email)
