import streamlit as st
import pandas as pd
import cv2
import numpy as np
import time
from ui_style import apply_modern_ui
from datetime import datetime
from navbar import show_navbar

apply_modern_ui()
show_navbar()

# -------- PAGE TITLE --------
st.title("Transactions")

# -------- AUTH CHECK --------
if "user" not in st.session_state:
    st.warning("Please login first")
    st.stop()

# -------- PANIC LOCK CHECK --------
if st.session_state.get("wallet_locked", False):
    st.error("🔒 Wallet is locked due to Panic Mode.")
    st.stop()

username = st.session_state["user"]

users = pd.read_csv("users.csv")
transactions = pd.read_csv("transactions.csv")

balance = users.loc[users["username"] == username, "balance"].values[0]

st.markdown(f'<div class="balance-text">Current Balance: ₹{balance}</div>', unsafe_allow_html=True)

# -------- PAYMENT METHOD --------
st.subheader("Select Payment Method")

payment_method = st.selectbox(
    "Payment Type",
    [
        "💼 Wallet",
        "🏦 Bank Transfer",
        "💳 Credit Card",
        "📱 UPI"
    ]
)

bank_name = "N/A"

if payment_method == "🏦 Bank Transfer":
    bank_name = st.selectbox(
        "Select Bank",
        [
            "State Bank of India (SBI)",
            "HDFC Bank",
            "ICICI Bank",
            "Axis Bank",
            "Punjab National Bank",
            "Bank of Baroda",
            "Kotak Mahindra Bank",
            "Canara Bank",
            "Union Bank of India",
            "IDFC First Bank"
        ]
    )

amount = st.number_input("Enter amount", min_value=1)

# -------- PAYMENT LOGIC --------
if st.button("Pay Now"):

    if amount <= balance:

        # Deduct balance
        users.loc[users["username"] == username, "balance"] -= amount
        users.to_csv("users.csv", index=False)

        # Save transaction
        new_txn = pd.DataFrame(
            [[username, amount, payment_method, bank_name, "approved", datetime.now()]],
            columns=["username", "amount", "method", "bank", "status", "date"]
        )

        transactions = pd.concat([transactions, new_txn], ignore_index=True)
        transactions.to_csv("transactions.csv", index=False)

        st.success("Transaction successful")

        # -------- Reverse Payment Feature --------
        st.session_state["last_transaction"] = {
            "amount": amount,
            "method": payment_method,
            "bank": bank_name,
            "time": time.time()
        }

    else:
        st.error("Insufficient balance")


# -------- UNDO FEATURE DISPLAY --------
if "last_transaction" in st.session_state:

    txn_time = st.session_state["last_transaction"]["time"]
    time_passed = time.time() - txn_time

    if time_passed < 10:
        st.warning("You can undo this transaction within 10 seconds.")

        if st.button("Undo Transaction"):

            amount = st.session_state["last_transaction"]["amount"]
            bank_name = st.session_state["last_transaction"]["bank"]

            # Refund balance
            users.loc[users["username"] == username, "balance"] += amount
            users.to_csv("users.csv", index=False)

            st.success("Transaction Reversed Successfully!")

            # -------- AI Risk Check --------
            risk_message = ""

            if amount > 2000:
                risk_message += "⚠ Large amount detected.\n"

            if bank_name != "N/A":
                risk_message += "⚠ Bank transfer detected.\n"

            current_hour = datetime.now().hour
            if current_hour < 6 or current_hour > 23:
                risk_message += "⚠ Late night transaction.\n"

            if risk_message:
                st.error("AI Risk Analysis:\n" + risk_message)
            else:
                st.info("AI Analysis: Transaction looked safe.")

            del st.session_state["last_transaction"]

    else:
        del st.session_state["last_transaction"]


# -------- TRANSACTION HISTORY --------
st.subheader("Transaction History")

user_txn = transactions[transactions["username"] == username]

if not user_txn.empty:
    user_txn["date"] = pd.to_datetime(user_txn["date"], errors="coerce")
    user_txn = user_txn.sort_values(by="date", ascending=False)
    st.dataframe(user_txn, use_container_width=True)
else:
    st.info("No transactions yet")

st.divider()

col1, col2 = st.columns(2)

with col1:
    if st.button("← Back to Dashboard"):
        st.switch_page("pages/1_Dashboard.py")

with col2:
    if st.button("Logout"):
        st.session_state.clear()
        st.switch_page("app.py")