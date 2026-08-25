import streamlit as st
import google.generativeai as genai

st.title("📓 Personal Journal Bot")
st.write("Welcome! This is your AI journal companion.")

# 1. Safely grab your API key from Streamlit Secrets or a sidebar input
api_key = st.sidebar.text_input("Enter your Gemini API Key:", type="password")

if not api_key:
    st.warning("Please enter your Gemini API key in the sidebar to start!")
else:
    # 2. Configure the Gemini API
    genai.configure(api_key=api_key)

    # 3. Initialize chat history in session state if it doesn't exist yet
    if "chat" not in st.session_state:
        model = genai.GenerativeModel("gemini-1.5-flash")
        st.session_state.chat = model.start_chat(history=[])

    # 4. Add a simple text input box
    user_input = st.text_input("Write a journal entry or ask a question:")

    if user_input:
        st.write(f"**You:** {user_input}")

        # 5. Send message to Gemini and get response
        try:
            response = st.session_state.chat.send_message(user_input)
            st.success(f"**Bot:** {response.text}")
    except Exception as e:
            st.error(f"An error occurred: {e}")
