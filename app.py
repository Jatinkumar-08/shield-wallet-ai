import streamlit as st
import pandas as pd

st.set_page_config(page_title="Shield Wallet", layout="wide")

logged_in = "user" in st.session_state

# ---------- STYLE ----------
if not logged_in:
    st.markdown("""
    <style>
    [data-testid="stSidebar"] {display: none;}

    /* Reduced top padding */
    .main .block-container {padding-top: 0.5rem;}

    .stApp {
        background: linear-gradient(135deg, #1E3C72, #2A5298);
    }

    /* Top header color */
    header[data-testid="stHeader"] {
        background: linear-gradient(135deg, #0F4C81, #2EC4B6);
    }

    /* Decorative top banner */
    .top-banner {
        width: 380px;
        height: 80px;
        margin: auto;
        margin-top: 20px;
        margin-bottom: 20px;
        border-radius: 16px;
        background: linear-gradient(135deg, #0F4C81, #2EC4B6);
        box-shadow: 0 10px 25px rgba(0,0,0,0.25);
        display: flex;
        align-items: center;
        justify-content: center;
        color: white;
        font-size: 20px;
        font-weight: bold;
    }

    /* Glassmorphism card */
    .login-card {
        backdrop-filter: blur(12px);
        background: rgba(255, 255, 255, 0.15);
        border-radius: 18px;
        padding: 40px;
        width: 380px;
        box-shadow: 0 10px 40px rgba(0,0,0,0.25);
        text-align: center;
    }

    /* Animated gradient shield logo */
    .shield-logo {
        font-size: 55px;
        font-weight: bold;
        background: linear-gradient(45deg, #2EC4B6, #00F5FF, #4FACFE);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        animation: pulse 2s infinite;
        margin-bottom: 8px;
        transition: transform 0.3s ease;
        cursor: pointer;
    }

    /* Hover effect */
    .shield-logo:hover {
        transform: scale(1.2) rotate(-5deg);
    }

    @keyframes pulse {
        0% { transform: scale(1); }
        50% { transform: scale(1.1); }
        100% { transform: scale(1); }
    }

    .title {
        font-size: 32px;
        font-weight: bold;
        color: white;
        margin-bottom: 5px;
    }

    .subtitle {
        color: #d0e4ff;
        margin-bottom: 25px;
    }

    /* Fix input visibility */
    input {
        color: black !important;
        background-color: white !important;
        border-radius: 8px !important;
    }

    label, .stCheckbox label {
    color: white !important;
    font-weight: 500;
    }


    /* Button */
    .stButton > button {
        background: linear-gradient(135deg, #0F4C81, #2EC4B6);
        color: white;
        border-radius: 10px;
        padding: 12px;
        font-weight: bold;
        width: 100%;
        border: none;
    }

    .stButton > button:hover {
        opacity: 0.9;
    }

    .link {
        color: #2EC4B6;
        font-size: 14px;
    }

    /* Remove empty elements */
    div:empty {
        display: none;
    }

    </style>
    """, unsafe_allow_html=True)

# ---------- LOAD USERS ----------
users = pd.read_csv("users.csv")

# ---------- LOGIN SCREEN ----------
if not logged_in:

    col1, col2, col3 = st.columns([1, 1, 1])

    with col2:
        # Decorative banner
        st.markdown('<div class="top-banner">💳 Smart • Secure • Fast</div>', unsafe_allow_html=True)

        # Login card
        st.markdown('<div class="login-card">', unsafe_allow_html=True)

        # Animated shield
        st.markdown('<div class="shield-logo">🛡</div>', unsafe_allow_html=True)
        st.markdown('<div class="title">Shield Wallet</div>', unsafe_allow_html=True)
        st.markdown('<div class="subtitle">Secure Digital Payments</div>', unsafe_allow_html=True)

        username = st.text_input("Username")
        password = st.text_input("Password", type="password")

        colA, colB = st.columns(2)

        with colA:
            remember = st.checkbox("Remember me")

        with colB:
            st.markdown('<div class="link">Forgot password?</div>', unsafe_allow_html=True)

        if st.button("Login", key="login_btn"):
            if username in users["username"].values:
                st.session_state["user"] = username
                st.success("Login successful")
                st.rerun()
            else:
                st.error("Invalid username or password")

        st.markdown('<br><div class="link">Create account</div>', unsafe_allow_html=True)

        st.markdown('</div>', unsafe_allow_html=True)

# ---------- REDIRECT AFTER LOGIN ----------
else:
    st.switch_page("pages/1_Dashboard.py")
