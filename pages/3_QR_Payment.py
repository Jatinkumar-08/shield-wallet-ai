import streamlit as st
import pandas as pd
import qrcode
from io import BytesIO
from datetime import datetime

# Import UI components
from navbar import show_navbar
from ui_style import apply_modern_ui
import verify_face

# Apply UI (only once!)
apply_modern_ui()
show_navbar()

st.title("💰 QR Payment")

# Check if user is logged in
if "user" not in st.session_state:
    st.warning("⚠️ Please login first")
    st.stop()

username = st.session_state["user"]

# Load data
try:
    users = pd.read_csv("users.csv")
    transactions = pd.read_csv("transactions.csv")
except FileNotFoundError:
    st.error("Database files not found!")
    st.stop()

# Get user balance
try:
    balance = users.loc[users["username"] == username, "balance"].values[0]
    st.success(f"💳 Wallet Balance: **₹{balance:,.2f}**")
except IndexError:
    st.error("User not found in database!")
    st.stop()

st.subheader("📱 Generate Payment QR")

# Large transaction threshold
LARGE_AMOUNT = 10000  # ₹10,000

# Payment form
amount = st.number_input("Enter amount (₹)", min_value=1, step=100, format="%d")

# Show warning for large transactions
if amount >= LARGE_AMOUNT:
    st.warning(f"⚠️ **LARGE TRANSACTION DETECTED: ₹{amount:,.2f}**")
    st.info("🔐 Face verification will be required for this payment")

# Generate QR button
if st.button("🔄 Generate QR", type="primary"):
    
    # STEP 1: Check for large transaction and verify face
    if amount >= LARGE_AMOUNT:
        st.info("📸 Face verification required for large transaction")
        
        # Call face verification
        with st.spinner("Verifying your identity..."):
            verified = verify_face.verify_face(username, amount)
        
        if not verified:
            st.error("❌ Transaction cancelled: Face verification failed")
            st.stop()
        else:
            st.success("✅ Face verified! Proceeding with payment...")
    
    # STEP 2: Generate QR code
    qr_data = f"user:{username}|amount:{amount}|time:{datetime.now()}"
    qr = qrcode.make(qr_data)
    
    buf = BytesIO()
    qr.save(buf, format="PNG")
    
    st.image(buf.getvalue(), caption="📷 Scan this QR code to pay", width=300)
    
    # Store in session state
    st.session_state['qr_amount'] = amount
    st.session_state['qr_generated'] = True

# STEP 3: Simulate Payment
if st.session_state.get('qr_generated', False):
    st.divider()
    st.subheader("💸 Complete Payment")
    
    col1, col2 = st.columns(2)
    
    with col1:
        if st.button("✅ Simulate Payment", type="primary", key="simulate_payment_btn"):
            amount_to_pay = st.session_state['qr_amount']
            
            if amount_to_pay <= balance:
                # Update balance
                users.loc[users["username"] == username, "balance"] -= amount_to_pay
                users.to_csv("users.csv", index=False)
                
                # Record transaction
                new_txn = pd.DataFrame(
                    [[username, amount_to_pay, "QR", "approved", datetime.now()]],
                    columns=["username", "amount", "method", "status", "date"]
                )
                transactions = pd.concat([transactions, new_txn], ignore_index=True)
                transactions.to_csv("transactions.csv", index=False)
                
                st.success(f"✅ Payment of ₹{amount_to_pay:,.2f} successful!")
                
                # Generate receipt
                receipt = f"""
                ═════════════════════════════
                SHIELD WALLET RECEIPT
                ═════════════════════════════
                User: {username}
                Amount: ₹{amount_to_pay:,.2f}
                Method: QR Payment
                Status: Approved
                Date: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}
                ═════════════════════════════
                Thank you for using Shield Wallet!
                """
                
                st.download_button(
                    label="📥 Download Receipt",
                    data=receipt,
                    file_name=f"receipt_{username}_{datetime.now().strftime('%Y%m%d_%H%M%S')}.txt",
                    mime="text/plain",
                    key="download_receipt_btn"
                )
                
                # Clear QR state
                st.session_state['qr_generated'] = False
                
            else:
                st.error(f"❌ Insufficient balance! Available: ₹{balance:,.2f}")
    
    with col2:
        if st.button("❌ Cancel", key="cancel_payment_btn"):
            st.session_state['qr_generated'] = False
            st.rerun()

# Show recent transactions
st.divider()
with st.expander("📊 Recent QR Transactions"):
    recent_qr = transactions[(transactions['username'] == username) & 
                             (transactions['method'] == 'QR')].tail(5)
    if not recent_qr.empty:
        st.dataframe(recent_qr[['date', 'amount', 'status']])
    else:
        st.info("No recent QR payments")