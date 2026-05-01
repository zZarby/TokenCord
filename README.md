# ⚡ TokenCord

TokenCord is a lightweight Discord client wrapper built with Python and `pywebview` that allows instant login using Discord tokens. It automates the injection process and manages your token lists efficiently.

## ✨ Features
* **Auto-Injection**: No need to open the console, the app handles `localStorage` injection.
* **Smart Parsing**: Supports both raw tokens and `email:pass:token` formats.
* **Token Queue**: Automatically removes the used token from your file after login.
* **Lightweight**: Minimalist interface without the overhead of a full browser.

## 🚀 Getting Started

### Prerequisites
* Python 3.8+
* pip

### Installation
1. Clone the repository:
```bash
git clone https://github.com/zZarby/TokenCord.git
cd TokenCord
```
2. Install dependencies:
```bash
pip install -r requirements.txt
```

### Usage
1. Run the script:
   ```bash
   python init.py
   ```
2. Select your `.txt` file containing the tokens.
3. Wait for the reload, and you're in!

## ⚠️ Disclaimer
This tool is for educational purposes only. Using Discord tokens to automate or access accounts can violate **Discord's Terms of Service**. Use it responsibly.
