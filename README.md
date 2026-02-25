# 🛡 Shield Wallet AI  
## Intelligent Secure Digital Wallet with AI Risk Detection

---

## 📌 Project Description

Shield Wallet AI is a secure digital wallet web application built using **Python and Streamlit**.

The purpose of this project is to simulate a real-world fintech payment platform that includes:
- Smart transaction handling
- AI-based risk detection
- Reverse payment (Undo system)
- Emergency wallet lock (Panic Button)
- Face verification for high-value transactions
- Credit card management
- Real-time transaction history

This project focuses on combining **user experience + security innovation**.

---

# 🎯 Problem Statement

Most digital wallets allow transactions but lack:
- Instant reversal capability
- Intelligent fraud detection
- Emergency account freeze option
- Risk analysis after suspicious activity

Shield Wallet AI attempts to solve these problems.

---

# 🧠 Core Innovations

## 1️⃣ Reverse Payment with AI Risk Analysis

After every transaction, the user gets a 10-second window to undo it.

If reversed, the system performs AI risk checks based on:
- Transaction amount
- Payment method (Bank transfer risk)
- Time of transaction (Late-night activity)

Example Risk Rules:
- Amount > ₹2000 → High risk
- Bank transfer → Medium risk
- Time between 12 AM – 6 AM → Suspicious activity
---

## 2️⃣ Panic Button Wallet Lock

Emergency feature that:
- Instantly locks wallet
- Blocks all transactions
- Requires manual unlock

Useful in case of:
- Phone theft
- Suspicious activity
- Unauthorized access

---

## 3️⃣ Face Verification for High Transactions

For large payments, the system:
- Captures live image
- Compares with stored user image
- Approves transaction only if similarity threshold matches

⚠ Note:
This uses basic image difference comparison (OpenCV).  
It is not production-grade facial recognition.

---

# 🏗 System Architecture

User  
↓  
Streamlit Frontend  
↓  
Transaction Logic  
↓  
CSV-based Storage  
↓  
AI Risk Engine  

Data Storage:
- users.csv
- cards.csv
- transactions.csv

---

## 🏗️ Project Architecture
secure_wallet/
├── app.py # Main application entry point
├── navbar.py # Navigation bar component
├── ui_style.py # UI styling and themes
├── register_face.py # Face registration module
├── verify_face.py # Face verification module
├── pages/ # Multi-page interface
│ ├── 1_Dashboard.py # Main dashboard
│ ├── 2_Transactions.py # Transaction history
│ ├── 3_QR_Payment.py # QR payment system
│ └── 4_Profile.py # User profile
├── assets/ # Static assets
│ ├── logo.png # App logo
│ └── banks/ # Bank logos
├── faces/ # Stored face encodings
└── data/ # CSV data files
├── users.csv # User credentials
├── transactions.csv # Transaction records
└── cards.csv # Card information

---

# ⚙ Technologies Used

- Python 3.10
- Streamlit
- Pandas
- NumPy
- OpenCV
- Git & GitHub

---

# 💻 Installation Guide

## Step 1: Clone Repository
git clone https://github.com/yourusername/shield-wallet-ai.git
cd shield-wallet-ai

## Step 2: Create Virtual Environment
python -m venv venv
venv\Scripts\activate

## Step 3: Install Dependencies
pip install -r requirements.txt

## Step 4: Run Application
streamlit run app.py

---

# 🌐 Deployment

The project can be deployed using:
- Streamlit Community Cloud
- Render
- Railway

⚠ Note:
Webcam-based face verification may not work on Streamlit Cloud.

---

# 🔐 Security Features
- Undo window protection
- Risk pattern detection
- Wallet freeze system
- High-value transaction verification

---

# ⚠ Limitations
- Uses CSV instead of database
- Face verification is basic pixel comparison
- No encryption for stored data
- No real payment gateway integration

---

# 🚀 Future Improvements
- Replace CSV with SQL database
- Implement real facial recognition using face_recognition library
- Add OTP verification
- Add encrypted password storage (bcrypt)
- Integrate real UPI / payment API
- Add fraud detection ML model
- Multi-user authentication system
- Email alerts for suspicious transactions

---

# 👨‍💻 Author
Jatinkumar GitHub: Jatinkumar-08

# 📈 Why This Project Is Valuable

This project demonstrates:
- Backend logic design
- AI-based risk modeling
- Security-focused development
- UI customization
- Git & GitHub workflow
- Deployment understanding

It is suitable for:
- Academic submission
- Internship portfolio
- Hackathon demo
- Resume project showcase

---

# ⭐ Final Note

Shield Wallet AI is a learning-focused fintech simulation project
designed to explore modern digital payment security systems.
