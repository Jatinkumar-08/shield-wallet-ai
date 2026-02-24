import streamlit as st
import pandas as pd
from ui_style import apply_modern_ui
apply_modern_ui()
from navbar import show_navbar
show_navbar()

st.title("Dashboard")

# -------- AUTH CHECK --------
if "user" not in st.session_state:
    st.warning("Please login first")
    st.stop()

# -------- PANIC LOCK SYSTEM --------
if "wallet_locked" not in st.session_state:
    st.session_state["wallet_locked"] = False

username = st.session_state["user"]

users = pd.read_csv("users.csv")
cards = pd.read_csv("cards.csv")

balance = users.loc[users["username"] == username, "balance"].values[0]

# ---------- Panic Button Section ----------
panic_col1, panic_col2 = st.columns([5,1])

with panic_col2:
    if st.button("🚨 Panic Lock", key="panic_btn"):
        st.session_state["wallet_locked"] = True
        st.error("Wallet Locked Instantly!")

if st.session_state["wallet_locked"]:
    st.warning("🔒 Wallet is currently LOCKED.")

    if st.button("Unlock Wallet", key="unlock_btn"):
        st.session_state["wallet_locked"] = False
        st.success("Wallet Unlocked Successfully!")

# ---------- Custom wallet style ----------
st.markdown("""
<style>
.wallet-card {
    background: linear-gradient(135deg, #0F4C81, #2EC4B6);
    padding: 25px;
    border-radius: 18px;
    color: white;
    font-size: 22px;
    font-weight: bold;
    text-align: center;
    box-shadow: 0 10px 30px rgba(0,0,0,0.3);
    transition: 0.3s ease;
}

.wallet-card:hover {
    transform: translateY(-5px) scale(1.02);
    box-shadow: 0 15px 40px rgba(0,0,0,0.4);
}

.wallet-amount {
    font-size: 32px;
    color: #E8FFF8;
    margin-top: 10px;
}
</style>
""", unsafe_allow_html=True)

# ---------- Top section ----------
col1, col2, col3 = st.columns([2, 2, 1])

with col1:
    st.markdown(
        f'''
        <div class="wallet-card">
            Wallet Balance
            <div class="wallet-amount">₹{balance}</div>
        </div>
        ''',
        unsafe_allow_html=True
    )

with col2:
    st.markdown('<div class="section-box">', unsafe_allow_html=True)
    st.subheader("Quick Add Money")

    c1, c2, c3 = st.columns(3)

    if c1.button("₹500", key="add500"):
        users.loc[users["username"] == username, "balance"] += 500
        users.to_csv("users.csv", index=False)
        st.success("₹500 added")
        st.rerun()

    if c2.button("₹1000", key="add1000"):
        users.loc[users["username"] == username, "balance"] += 1000
        users.to_csv("users.csv", index=False)
        st.success("₹1000 added")
        st.rerun()

    if c3.button("₹2000", key="add2000"):
        users.loc[users["username"] == username, "balance"] += 2000
        users.to_csv("users.csv", index=False)
        st.success("₹2000 added")
        st.rerun()

    st.markdown('</div>', unsafe_allow_html=True)

with col3:
    if st.button("Logout", key="dash_logout"):
        st.session_state.clear()
        st.switch_page("app.py")

# ---------- Add card section ----------
st.subheader("Add Credit Card")
card_number = st.text_input("Card Number")
expiry = st.text_input("Expiry (MM/YY)")
limit = st.number_input("Credit Limit", value=50000)

if st.button("Add Card", key="add_card_btn"):
    if card_number:
        last4 = card_number[-4:]
        new_card = pd.DataFrame(
            [[username, last4, expiry, limit, 0]],
            columns=["username", "card_last4", "expiry", "limit", "used"]
        )
        cards = pd.concat([cards, new_card], ignore_index=True)
        cards.to_csv("cards.csv", index=False)
        st.success("Card added successfully")
    else:
        st.error("Enter card number")

# ---------- Show cards ----------
user_cards = cards[cards["username"] == username]
if not user_cards.empty:
    st.subheader("Your Cards")
    for _, card in user_cards.iterrows():
        st.info(f"**** **** **** {card['card_last4']} (Expiry: {card['expiry']})")

# ---------- Next button ----------
st.divider()
if st.button("Go to Transactions →", key="go_txn"):
    st.switch_page("pages/2_Transactions.py")