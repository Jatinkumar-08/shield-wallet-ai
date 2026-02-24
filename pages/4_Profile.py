import streamlit as st
import pandas as pd
from ui_style import apply_modern_ui
apply_modern_ui()
from navbar import show_navbar
import os

show_navbar()
st.title("User Profile")

if "user" not in st.session_state:
    st.warning("Please login first")
    st.stop()

username = st.session_state["user"]
users = pd.read_csv("users.csv")

user_row = users[users["username"] == username].iloc[0]

st.subheader(f"Welcome, {username}")

# Profile photo
photo_path = user_row.get("photo", "")

if isinstance(photo_path, str) and photo_path and os.path.exists(photo_path):
    st.image(photo_path, width=150, caption="Profile Photo")
else:
    st.info("No profile photo uploaded")

uploaded = st.file_uploader("Upload Profile Photo", type=["png", "jpg", "jpeg"])

if uploaded:
    os.makedirs("profile_photos", exist_ok=True)
    save_path = f"profile_photos/{username}.png"

    with open(save_path, "wb") as f:
        f.write(uploaded.getbuffer())

    users.loc[users["username"] == username, "photo"] = save_path
    users.to_csv("users.csv", index=False)

    st.success("Profile photo updated")
    st.rerun()

st.subheader("Account Info")
st.write(f"Balance: ₹{user_row['balance']}")
st.write(f"Face Registered: {user_row['face_registered']}")
