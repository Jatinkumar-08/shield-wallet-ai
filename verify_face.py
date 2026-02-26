import streamlit as st 
import os 
from PIL import Image 
 
def verify_face(username, amount=None): 
    \"\"\"Simplified verification without OpenCV\"\"\" 
    stored_path = f"faces/{username}.jpg" 
 
    if not os.path.exists(stored_path): 
        st.error("? No registered face found") 
        return False 
 
    if amount and amount 
        st.warning(f"?? Large transaction: ?{amount}") 
        st.info("?? Camera would open here (OpenCV not available on cloud)") 
        # For demo, just approve 
        if st.button("Click to simulate face verification"): 
            st.success("? Face verified!") 
            return True 
        return False 
 
    return True 
