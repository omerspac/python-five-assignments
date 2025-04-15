import streamlit as st

st.set_page_config("Omer Growth Mindset Project", project_icon="🌟")
st.title("Growth Mindset Challenge: Web App With Streamlit")

#head-section
st.header("🚀 Welcome To Your Growth Journey!")
st.write("Embrace challenges, learn from mistakes and unlock your full potential. This AI application will help you in building a growth mindset with reflection, challenges and achievements!")

#quote-section
st.header("Todays Growth Mindset Quote")
st.write("\"The greater the difficulty, the more the glory in surmounting it.\"- Epicurus")

st.header("What's Your Challenge Today?")
user_input = st.text_input("Describe the challenge you're currently facing:")

if user_input:
    st.success(f"Hmm! {user_input}. Keep pushing forward and don't give up!")
else:
    st.warning("Whats your challenge, so we can get started.")

#reflection
st.header("Reflect On Your Learning")
reflection = st.text_area("Write your reflection here:")

if reflection:
    st.success(f"✨Great Insight! Your reflection: {reflection}")
else:
    st.info("Reflection on past experience helps you to grow! Share your hardships.")

#achievements
st.header("🏆 Celebrate Your Wins!")
achievements = st.text_input("Share something, you've recently accomplished:")

if achievements:
    st.success(f"🌠 Amazing! You achieved: {achievements}")

else:
    st.info("Doesn't matter if small or big, every achievement **counts**. ✨ Please share!")

#footer
st.write("- - -")
st.write("🚀 Keep believing yourself. Growth is a journey, not a destination! ☀️")
st.write("**Created by: Muhammad Omer**")