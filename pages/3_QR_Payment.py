import streamlit as st
import pandas as pd
import qrcode
from ui_style import apply_modern_ui
apply_modern_ui()
from io import BytesIO
from datetime import datetime
from navbar import show_navbar
show_navbar()

st.title("QR Payment")

if "user" not in st.session_state:
    st.warning("Please login first")
    st.stop()

username = st.session_state["user"]

users = pd.read_csv("users.csv")
transactions = pd.read_csv("transactions.csv")

balance = users.loc[users["username"] == username, "balance"].values[0]

st.success(f"Wallet Balance: ₹{balance}")

st.subheader("Generate Payment QR")

amount = st.number_input("Enter amount", min_value=1)

if st.button("Generate QR"):

    qr_data = f"user:{username}|amount:{amount}"
    qr = qrcode.make(qr_data)

    buf = BytesIO()
    qr.save(buf, format="PNG")

    st.image(buf.getvalue(), caption="Scan to Pay", width=200)

    if st.button("Simulate Payment"):
        if amount <= balance:
            users.loc[users["username"] == username, "balance"] -= amount
            users.to_csv("users.csv", index=False)

            new_txn = pd.DataFrame(
                [[username, amount, "QR", "approved", datetime.now()]],
                columns=["username", "amount", "method", "status", "date"]
            )
            transactions = pd.concat([transactions, new_txn], ignore_index=True)
            transactions.to_csv("transactions.csv", index=False)

            st.success("QR Payment successful")
            from datetime import datetime

            receipt = f"""
            SHIELD WALLET RECEIPT
            -------------------------
            User: {username}
            Amount: ₹{amount}
            Method: QR Payment
            Status: Approved
            Date: {datetime.now()}
            """

            st.download_button(
            label="Download Receipt",
            data=receipt,
            file_name="qr_receipt.txt",
            mime="text/plain"
        )
        else:
            st.error("Insufficient balance")
