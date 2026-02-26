from ui_style import apply_modern_ui
apply_modern_ui() 
from navbar import show_navbar
show_navbar()
apply_modern_ui()
show_navbar()

# -------- PAGE TITLE --------
st.title("💰 Transactions")

# -------- AUTH CHECK --------
if "user" not in st.session_state:
    st.warning("⚠️ Please login first")
    st.stop()

# -------- PANIC LOCK CHECK --------
if st.session_state.get("wallet_locked", False):
    st.error("🔒 Wallet is locked due to Panic Mode.")
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
    st.markdown(f'<div class="balance-text">💳 Current Balance: **₹{balance:,.2f}**</div>', unsafe_allow_html=True)
except IndexError:
    st.error("User not found in database!")
    st.stop()

# -------- LARGE TRANSACTION THRESHOLD --------
LARGE_AMOUNT = 10000  # ₹10,000

# -------- PAYMENT METHOD --------
st.subheader("📋 Select Payment Method")

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

amount = st.number_input("Enter amount (₹)", min_value=1, step=100, format="%d")

# Show warning for large transactions
if amount >= LARGE_AMOUNT:
    st.warning(f"⚠️ **LARGE TRANSACTION DETECTED: ₹{amount:,.2f}**")
    st.info("🔐 Face verification will be done automatically")

# -------- PAYMENT LOGIC WITH AUTO FACE VERIFICATION --------
if st.button("💸 Pay Now", type="primary"):

    if amount <= balance:
        
        # STEP 1: Check for large transaction and verify face automatically
        if amount >= LARGE_AMOUNT:
            st.info("📸 **Auto face verification in progress...**")
            st.markdown("🔵 Please look at the camera. Verification will happen automatically.")
            
            # Call face verification (auto-capture version)
            with st.spinner("🔄 Initializing camera..."):
                verified = verify_face.verify_face(username, amount)
            
            if not verified:
                st.error("❌ Transaction cancelled: Face verification failed")
                st.stop()  # Stop execution
            else:
                st.success("✅ Face verified! Processing payment...")
        
        # STEP 2: Process payment (only if verified or small amount)
        
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

        st.success(f"✅ Transaction of ₹{amount:,.2f} successful!")
        
        # Store for undo feature
        st.session_state["last_transaction"] = {
            "amount": amount,
            "method": payment_method,
            "bank": bank_name,
            "time": time.time(),
            "verified": amount >= LARGE_AMOUNT  # Track if face verified
        }

    else:
        st.error(f"❌ Insufficient balance! Available: ₹{balance:,.2f}")

# -------- UNDO FEATURE DISPLAY --------
if "last_transaction" in st.session_state:

    txn_time = st.session_state["last_transaction"]["time"]
    time_passed = time.time() - txn_time

    if time_passed < 10:
        st.warning("⏰ You can undo this transaction within 10 seconds.")
        
        # Show if it was a face-verified transaction
        if st.session_state["last_transaction"].get("verified", False):
            st.caption("🔐 This was a large transaction that required face verification")

        if st.button("↩️ Undo Transaction"):

            amount = st.session_state["last_transaction"]["amount"]
            bank_name = st.session_state["last_transaction"]["bank"]

            # Refund balance
            users.loc[users["username"] == username, "balance"] += amount
            users.to_csv("users.csv", index=False)

            st.success("✅ Transaction Reversed Successfully!")

            # -------- AI Risk Check (Only for reversed transactions) --------
            risk_message = []
            
            if amount > 2000:
                risk_message.append("⚠ Large amount detected")
            
            if bank_name != "N/A":
                risk_message.append("⚠ Bank transfer detected")
            
            current_hour = datetime.now().hour
            if current_hour < 6 or current_hour > 23:
                risk_message.append("⚠ Late night transaction")
            
            # Add face verification status to risk analysis
            if st.session_state["last_transaction"].get("verified", False):
                risk_message.append("✅ Face verified transaction")
            
            st.subheader("🤖 AI Risk Analysis")
            if risk_message:
                for msg in risk_message:
                    if "✅" in msg:
                        st.success(msg)
                    else:
                        st.error(msg)
            else:
                st.info("✅ Transaction looked safe.")

            del st.session_state["last_transaction"]

    else:
        del st.session_state["last_transaction"]

# -------- TRANSACTION HISTORY --------
st.divider()
st.subheader("📊 Transaction History")

user_txn = transactions[transactions["username"] == username]

if not user_txn.empty:
    user_txn["date"] = pd.to_datetime(user_txn["date"], errors="coerce")
    user_txn = user_txn.sort_values(by="date", ascending=False)
    
    # Add a visual indicator for large transactions
    def highlight_large(val):
        if isinstance(val, (int, float)) and val >= LARGE_AMOUNT:
            return 'background-color: #ffebee; color: #c62828'
        return ''
    
    st.dataframe(
        user_txn.style.applymap(highlight_large, subset=['amount']),
        use_container_width=True,
        height=400
    )
    
    # Summary stats
    total_spent = user_txn['amount'].sum()
    large_txns = user_txn[user_txn['amount'] >= LARGE_AMOUNT].shape[0]
    
    col1, col2, col3 = st.columns(3)
    with col1:
        st.metric("Total Spent", f"₹{total_spent:,.2f}")
    with col2:
        st.metric("Total Transactions", len(user_txn))
    with col3:
        st.metric("Large Transactions", large_txns)
else:
    st.info("📭 No transactions yet")

st.divider()

# -------- NAVIGATION --------
col1, col2, col3 = st.columns(3)

with col1:
    if st.button("← Back to Dashboard"):
        st.switch_page("pages/1_Dashboard.py")

with col2:
    if st.button("📱 Go to QR Payment"):
        st.switch_page("pages/3_QR_Payment.py")

with col3:
    if st.button("🚪 Logout"):
        st.session_state.clear()
        st.switch_page("app.py")
