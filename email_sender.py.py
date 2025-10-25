import smtplib, time
from email.mime.text import MIMEText

def send_gmail(sender, password, receiver, subject, body, retries=2):
    msg = MIMEText(body)
    msg['From'], msg['To'], msg['Subject'] = sender, receiver, subject

    for i in range(retries + 1):
        try:
            with smtplib.SMTP('smtp.gmail.com', 587) as s:
                s.starttls()
                s.login(sender, password)
                s.send_message(msg)
            print("✅ Email sent")
            return True
        except Exception as e:
            print(f"⚠️ Attempt {i+1} failed: {e}")
            if i < retries:
                print("Retrying in 5s...")
                time.sleep(5)
    print("❌ Failed to send")
    return False

if __name__ == "__main__":
    sender = input("Sender: ")
    password = input("App Password: ")
    receiver = input("Receiver: ")
    subject = input("Subject: ")
    message = input("Message: ")

    send_gmail(sender, password, receiver, subject, message)
    input("Press Enter to exit...")
