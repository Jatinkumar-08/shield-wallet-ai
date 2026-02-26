import streamlit as st
import os

def verify_face(username, amount=None):
    """Face verification without OpenCV"""
    stored_path = f"faces/{username}.jpg"
    
    if not os.path.exists(stored_path):
        st.error("? No registered face found")
        return False
    
    if amount and amount >= 10000:
        st.warning(f"?? Large transaction: ?{amount}")
        st.info("?? Camera would open here (simulated)")
        
        # Simple button-based verification
        col1, col2 = st.columns(2)
        with col1:
            if st.button("? Approve", key=f"approve_{username}"):
                st.success("? Transaction approved")
                return True
        with col2:
            if st.button("? Cancel", key=f"cancel_{username}"):
                st.error("Transaction cancelled")
                return False
        return False
    
    return True