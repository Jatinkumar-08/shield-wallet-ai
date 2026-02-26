import streamlit as st 
import os 
from datetime import datetime 
 
def verify_face(username, amount=None): 
    \"\"\"Face verification without OpenCV\"\"\" 
    stored_path = f"faces/{username}.jpg" 
 
    if not os.path.exists(stored_path): 
        st.error("? Please register your face first in Profile page") 
        return False 
 
    if amount and amount 
        st.warning(f"?? **LARGE TRANSACTION: ?{amount}**") 
        st.info("Face verification required") 
 
        col1, col2 = st.columns(2) 
        with col1: 
            if st.button("? Approve Transaction"): 
                st.success("û Transaction approved") 
                return True 
        with col2: 
            if st.button("? Cancel"): 
                st.error("Transaction cancelled") 
                return False 
        return False 
 
    return True 
