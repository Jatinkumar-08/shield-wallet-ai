# 🔐 Secure Wallet - AI-Powered Digital Wallet with Face Recognition

Secure Wallet is an advanced digital wallet application that leverages face recognition technology for secure authentication and seamless transactions. Built with Python and a user-friendly interface, this application provides a modern approach to digital payments and personal finance management.

## ✨ Key Features

• **Face Recognition Authentication** - Secure login using facial recognition technology with real-time verification
• **QR Code Payments** - Generate and scan QR codes for instant peer-to-peer transactions
• **Multi-Bank Support** - Integrated with major Indian banks (Axis, HDFC, ICICI, SBI)
• **Transaction Dashboard** - Real-time tracking and visualization of all financial activities
• **User Profile Management** - Personalized profiles with face registration and account settings
• **CSV-Based Data Storage** - Lightweight and portable data management using CSV files

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

text

## 🚀 Quick Start Guide

1. **Clone the repository**
   ```bash
   git clone https://github.com/Jatinkumar-08/shield-wallet-ai.git
   cd shield-wallet-ai
Install dependencies

bash
pip install -r requirements.txt
Run the application

bash
python app.py
Access the app - Open your browser and navigate to http://localhost:5000

📋 Prerequisites
Python 3.8 or higher
Webcam for face recognition
Internet connection for QR payments
Modern web browser (Chrome/Firefox/Edge)


🛠️ Technologies Used
Python 3.10 - Core programming language
Face Recognition Library - Facial authentication
OpenCV - Real-time face detection
Flask/Streamlit - Web framework (adjust based on your actual framework)
Pandas - Data management
HTML/CSS - Frontend styling
QR Code Library - Payment QR generation


💡 How It Works
Registration - New users register their face and create an account
Login - Face recognition verifies identity in real-time
Dashboard - View balance, recent transactions, and quick actions
Payments - Generate QR codes or scan to transfer money
History - Track all transactions with filters and search

🔒 Security Features
Biometric face recognition for authentication
Local data storage (no cloud dependencies)
Encrypted face encodings
Session management
Secure QR code generation


🤝 Contributing
Contributions are welcome! Feel free to fork this repository and submit pull requests. For major changes, please open an issue first to discuss what you'd like to change.


📧 Contact & Support
GitHub: @Jatinkumar-08
Repository: shield-wallet-ai

📄 License
This project is developed for educational and portfolio purposes. All rights reserved.

🙏 Acknowledgments
Thanks to the Python community for amazing libraries
Inspired by modern digital wallet applications
Built as a demonstration of AI integration in fintech

