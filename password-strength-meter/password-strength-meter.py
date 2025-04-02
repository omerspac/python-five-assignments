import re
import streamlit as st

st.set_page_config(page_title="Password Strength Meter By Muhammad Omer", page_icon="🔐", layout="centered")

st.markdown("""
<style>
    .main {text-align: center;}
    .stTextInput {margin: auto; }       
    .stButton button {width: 40%; background-color: white; color: black; font-size: 18px; margin-left: 30%;}
    .stButton button:hover {background-color: black; color: white;}
</style>
""", unsafe_allow_html=True)

st.title("🔐 Password Strength Checker")
st.write("Enter your password below to check its strength! 🔍")

def check_password_strength(password):
    score = 0
    feedback = []

    # Length Check
    if len(password) >= 8:
        score += 1
    else:
        feedback.append("❌ Password should be **at least** 8 characters long.")
    
    # Upper & Lowercase Check
    if re.search(r"[A-Z]", password) and re.search(r"[a-z]", password):
        score += 1
    else:
        feedback.append("❌ Include **both** uppercase and lowercase letters.")
    
    # Digit Check
    if re.search(r"\d", password):
        score += 1
    else:
        feedback.append("❌ Add at least one number (0-9).")

    # Special Character Check
    if re.search(r"[!@#$%^&*]", password):
        score += 1
    else:
        feedback.append("❌ Include at least one special character (!@#$%^&*).")
    
    return score, feedback # Return

# Input field
password = st.text_input("Enter your password: ", type="password", help="Ensure your password is strong! 🔐")

# Button to check password strength
if st.button("Check Strength"):
    if password:
        score, feedback = check_password_strength(password)  # Get

        # Displaying strength rating
        if score == 4:
            st.success("✅ Strong Password!")
        elif score == 3:
            st.info("⚠️ Moderate Password - Consider adding more security features.")
        else:
            st.error("❌ Weak Password - Improve it using the suggestions below.")

        # Showing improvement tips
        if feedback:
            with st.expander("Improve your password"):
                for item in feedback:
                    st.write(item)
    else:
        st.warning("⚠️ Please enter a password first!")