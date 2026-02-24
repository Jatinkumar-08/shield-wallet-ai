import streamlit as st

def show_navbar():
    st.markdown(
    '<div class="ticker"><span>🔒 Secure Payments • Instant Transfers • AI Fraud Protection • Welcome to Shield Wallet</span></div>',
    unsafe_allow_html=True
    )

    st.markdown("""
    <style>
    .nav-container {
        background-color: #0a3d62;
        padding: 10px 15px;
        border-radius: 10px;
        margin-bottom: 20px;
    }
    .nav-title {
        color: white;
        font-size: 22px;
        font-weight: bold;
    }
    .ticker {
        background: linear-gradient(90deg, #0F4C81, #2EC4B6);
        color: white;
        padding: 6px;
        border-radius: 8px;
        margin-bottom: 10px;
        font-size: 14px;
        overflow: hidden;
        white-space: nowrap;
    }

    .ticker span {
        display: inline-block;
        padding-left: 100%;
        animation: ticker 12s linear infinite;
    }

    @keyframes ticker {
        0% { transform: translateX(0); }
        100% { transform: translateX(-100%); }
    }
    </style>
    """, unsafe_allow_html=True)

    col1, col2, col3, col4, col5, col6 = st.columns([3,1,1,1,1,1])

    with col1:
        st.markdown('<div class="nav-title">🛡 SHIELD Wallet</div>', unsafe_allow_html=True)

    with col2:
        if st.button("🏠", key="nav_dashboard", help="Dashboard"):
            st.switch_page("pages/1_Dashboard.py")

    with col3:
        if st.button("💳", key="nav_transactions", help="Transactions"):
            st.switch_page("pages/2_Transactions.py")

    with col4:
        if st.button("📷", key="nav_qr", help="QR Pay"):
            st.switch_page("pages/3_QR_Payment.py")

    with col5:
        if st.button("👤", key="nav_profile", help="Profile"):
           st.switch_page("pages/4_Profile.py")

    with col6:
        if st.button("🚪", key="nav_logout", help="Logout"):
           st.session_state.clear()
           st.switch_page("app.py")
