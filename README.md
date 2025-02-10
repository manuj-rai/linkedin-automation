# 🚀 LinkedIn Invitation Withdraw Script

## 📌 Overview
This script automates the withdrawal of sent connection requests on LinkedIn using **Selenium** and **WebDriver Manager**. It scrolls through the "Sent Invitations" page and withdraws pending connection requests.

⚠ **Use this script responsibly!** Excessive automation can lead to account restrictions.

---

## 🛠 Installation & Setup

### **1️⃣ Install Dependencies**
Run the following command to install the required dependencies:
```bash
pip install selenium webdriver-manager
```

### **2️⃣ WebDriver Setup**
The script uses `webdriver-manager` to automatically manage the ChromeDriver. Make sure you have Google Chrome installed.

### **3️⃣ Usage**
Replace your LinkedIn credentials inside the script:
```python
LINKEDIN_EMAIL = "your_email"
LINKEDIN_PASSWORD = "your_password"
```

Then, run the script:
```bash
python linkedin_withdraw.py
```

---

## ⚠ Important Notes

### **🔴 Use with Caution**
- LinkedIn may **restrict your account** for excessive automation.
- Consider using **OAuth or cookies** instead of direct login credentials for enhanced security.
- Modify `time.sleep(x)` delays to avoid detection.
- Avoid running the script too frequently to prevent triggering LinkedIn’s security systems.

---

## 🏆 Features
✅ **Automated Login** – Logs into LinkedIn securely.
✅ **Auto Scrolling** – Loads all sent invitations dynamically.
✅ **Bulk Withdrawals** – Withdraws all sent connection requests.
✅ **Error Handling** – Includes exception handling for reliability.

---

## 🛡 Disclaimer
This script is for **educational purposes only**. Use at your own risk. LinkedIn’s policies may restrict automation, and excessive usage can lead to account limitations.

**Happy Coding! 🚀**

