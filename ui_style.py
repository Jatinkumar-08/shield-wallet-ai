import streamlit as st

def apply_modern_ui():

    st.markdown("""
    <style>

    /* Animated gradient background */
    .stApp {
        background: linear-gradient(135deg, #0f2027, #203a43, #2c5364);
        background-size: 400% 400%;
        animation: gradientBG 12s ease infinite;
    }

    @keyframes gradientBG {
        0% { background-position: 0% 50%; }
        50% { background-position: 100% 50%; }
        100% { background-position: 0% 50%; }
    }

    /* Colorful sidebar */
    [data-testid="stSidebar"] {
        background: linear-gradient(180deg, #0F4C81, #2EC4B6);
        border-right: none;
    }

    /* Sidebar text */
    [data-testid="stSidebar"] * {
        color: white !important;
        font-weight: 500;
    }

    /* Sidebar items hover */
    [data-testid="stSidebar"] a:hover {
        background: rgba(255, 255, 255, 0.15);
        border-radius: 8px;
        transform: translateX(3px);
    }

    /* Top navbar */
    header[data-testid="stHeader"] {
        background: linear-gradient(135deg, #0F4C81, #2EC4B6);
    }

    /* Glass cards */
    .glass-card {
        backdrop-filter: blur(12px);
        background: rgba(255, 255, 255, 0.12);
        border-radius: 18px;
        padding: 25px;
        box-shadow: 0 15px 35px rgba(0,0,0,0.25);
        margin-bottom: 20px;
    }

    /* Headings */
    h1, h2, h3, h4 {
        color: white !important;
    }

    /* Wallet balance */
    .wallet-balance {
        font-size: 26px;
        font-weight: bold;
        color: #2EC4B6 !important;
    }

    /* General readable text */
    p, label {
        color: #e0f2ff !important;
    }

    /* Buttons */
    .stButton > button {
        background: linear-gradient(135deg, #2EC4B6, #4FACFE);
        color: white;
        border-radius: 10px;
        padding: 10px 16px;
        border: none;
        font-weight: bold;
    }

    .stButton > button:hover {
        transform: scale(1.03);
        transition: 0.2s;
    }

    /* Inputs */
    input, textarea {
        border-radius: 8px !important;
        color: black !important;
        background-color: white !important;
    }

    /* Number input */
    [data-testid="stNumberInput"] input {
        color: black !important;
        background-color: white !important;
    }

    /* File uploader visibility */
    [data-testid="stFileUploader"] {
        background: rgba(255, 255, 255, 0.9);
        border-radius: 10px;
        padding: 10px;
    }

    [data-testid="stFileUploader"] * {
        color: #1f2d3d !important;
    }

    /* Success receipt animation */
    .success-receipt {
        background: linear-gradient(135deg, #2EC4B6, #4FACFE);
        color: white;
        padding: 25px;
        border-radius: 16px;
        text-align: center;
        font-size: 20px;
        font-weight: bold;
        box-shadow: 0 15px 35px rgba(0,0,0,0.25);
        animation: popIn 0.6s ease;
        margin-top: 20px;
    }

    @keyframes popIn {
        0% { transform: scale(0.7); opacity: 0; }
        100% { transform: scale(1); opacity: 1; }
    }

    /* Tooltip styling */
    [data-baseweb="tooltip"] {
        background-color: #0F4C81 !important;
        color: white !important;
        border-radius: 8px;
        font-size: 14px;
    }

    /* Icon hover */
    .nav-icon:hover {
        transform: scale(1.1);
        background: linear-gradient(135deg, #0F4C81, #2EC4B6);
        color: white !important;
    }

    /* =========================
       SELECTBOX VISIBILITY FIX
       ========================= */

    /* Main selectbox */
    [data-baseweb="select"] {
        background-color: white !important;
        color: black !important;
    }

    /* Text inside selectbox */
    [data-baseweb="select"] * {
        color: black !important;
        font-weight: 600 !important;
    }

    /* Dropdown options */
    div[role="option"] {
        color: black !important;
        background-color: white !important;
        font-weight: 600 !important;
    }

    /* Hover on options */
    div[role="option"]:hover {
        background-color: #e6f2ff !important;
        color: black !important;
    }

    /* Transaction table */
    [data-testid="stDataFrame"] {
        color: black !important;
        background-color: white !important;
    }

    /* Table headers */
    thead tr th {
        color: black !important;
        background-color: #f1f1f1 !important;
        font-weight: bold;
    }

    </style>
    """, unsafe_allow_html=True)
