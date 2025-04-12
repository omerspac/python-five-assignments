import streamlit as st
import hashlib
from hashlib import pbkdf2_hmac
import json, os, time
from cryptography.fernet import Fernet
from base64 import urlsafe_b64encode

# DATA OF USER
DATA_FILE = "secure_data.json"
SALT = b"secure_salt_value"
LOCKOUT_DURATION = 60

# LOGIN DETAILS
if "authenticated_user" not in st.session_state:
    st.session_state.authenticated_user = None

if "failed_attempt" not in st.session_state:
    st.session_state.failed_attempt = 0

if "lockout_time" not in st.session_state:
    st.session_state.lockout_time = 0

# IF DATA IS LOADED
def load_data():
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, "r") as f:
            return json.load(f)
    return{}
    
def save_data(data):
    with open(DATA_FILE, "w") as f:
        json.dump(data, f)
    
def generate_key(passkey):
    key = pbkdf2_hmac('sha256', passkey.encode(), SALT, 100000)
    return urlsafe_b64encode(key)

def hash_password(password):
    return hashlib.pbkdf2_hmac('sha256', password.encode(), SALT, 100000).hex()

# cryptography.fernet USED
def encrypt_text(text, key):
    cipher = Fernet(generate_key(key))
    return cipher.encrypt(text.encode()).decode()

def decrypt_text(encrypt_text, key):
    try:
        cipher = Fernet(generate_key(key))
        return cipher.decrypt(encrypt_text.encode()).decode()
    except:
        return None
    
stored_data = load_data()

# Streamlit UI
st.title("🔒 Secure Data Encryption System")

# NAVIGATION BAR
menu = ["Home", "Register",  "Login", "Store Data", "Retrieve Data"]
choice = st.sidebar.selectbox("Navigation", menu)

if choice == "Home":
    st.subheader("🏠 Welcome to the Secure Data System")
    st.write("Use this app to **securely store and retrieve data** using unique passkeys.")

# REGISTER
elif choice == "Register":
    st.subheader("✏️ Register New User")
    username = st.text_input("Choose Username")
    password = st.text_input("Choose Password", type="password")

    if st.button("Register"):
        if username and password:
            if username in stored_data:
                st.warning("⚠️ User already exists!")

            else:
                stored_data[username] = {
                    "password": hash_password(password),
                    "data": []
                }
                save_data(stored_data)
                st.success("✅ User register successfully")
        else:
            st.error("Both fields are required.")

    elif choice == "Login":
        st.subheader("🔑 User Login")

        if time.time() < st.session_state.lockout_time:
            remaining = int(st.session_state.lockout_time - time.time())
            st.error(f"⏱️ Too many failed attempts! Please wait {remaining} seconds.")
            st.stop()

        username = st.text_input("Username")
        password = st.text_input("Password", type="password")

        if st.button("Login"):
            if username in stored_data and stored_data[username]["password"] == hash_password(password):
                st.session_state.authenticated_user = username
                st.session_state.failed_attempt = 0
                st.success(f"✅ Welcome {username}")
            else:
                st.session_state.failed_attempts += 1
                remaining = 3 - st.session_state.failed_attempts
                st.error(f"❌ Invalid Credentials! Attempts left: {remaining}")

                if st.session_state.failed_attempt >= 3:
                    st.session_state.lockout_time = time.time() + LOCKOUT_DURATION
                    st.error("🛑 Too many failed attempts. Locked for 60 seconds")
                    st.stop()
                    
# STORE DATA
elif choice == "Store Data":
    st.subheader("📂 Store Data Securely")
    user_data = st.text_area("Enter Data:")
    passkey = st.text_input("Enter Passkey:", type="password")

    if st.button("Encrypt & Save"):
        if user_data and passkey:
            hashed_passkey = hash_password(passkey)
            encrypted_text = encrypt_text(user_data, passkey)
            stored_data[encrypted_text] = {"encrypted_text": encrypted_text, "passkey": hashed_passkey}
            st.success("✅ Data stored securely!")
        else:
            st.error("⚠️ Both fields are required!")

# RETREIVE DATA
elif choice == "Retrieve Data":
    st.subheader("🔍 Retrieve Your Data")
    encrypted_text = st.text_area("Enter Encrypted Data:")
    passkey = st.text_input("Enter Passkey:", type="password")

    if st.button("Decrypt"):
        if encrypted_text and passkey:
            decrypted_text = decrypt_text(encrypted_text, passkey)

            if decrypted_text:
                st.success(f"✅ Decrypted Data: {decrypted_text}")
            else:
                st.error(f"❌ Incorrect passkey! Attempts remaining: {3 - st.session_state.failed_attempt}")

                if st.session_state.failed_attempt >= 3:
                    st.warning("🔒 Too many failed attempts! Redirecting to Login Page.")
                    st.experimental_rerun()
        else:
            st.error("⚠️ Both fields are required!")