# main.py
from auth import authenticate_user
from otp_module import send_otp_email, is_otp_valid, resend_otp

def main():
    print("===== Two-Factor Authentication Demo (RSA Encrypted OTP) =====")
    username = input("Enter Username: ")
    password = input("Enter Password: ")

    if authenticate_user(username, password):
        print("Login successful! Proceeding to OTP verification...\n")
        email = input("Enter your registered email: ")
        send_otp_email(email)

        while True:
            user_otp = input("\nEnter Decrypted OTP (or type 'resend' to get new OTP): ")
            if user_otp.lower() == "resend":
                resend_otp(email)
                continue
            valid, message = is_otp_valid(user_otp)
            print(message)
            if valid:
                print("Access Granted! Welcome to the system.")
                break
            elif "expired" in message.lower():
                resend_choice = input("OTP expired. Type 'resend' to get new OTP: ")
                if resend_choice.lower() == "resend":
                    resend_otp(email)
    else:
        print("X Invalid username or password.")

if __name__ == "__main__":
    main()
