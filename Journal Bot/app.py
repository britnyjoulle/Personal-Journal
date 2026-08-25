import streamlit as st
from google import genai
from google.genai import types

st.set_page_config(page_title="Intellectual Journal Vault", page_icon="🧠", layout="centered")
st.title("🧠 Intellectual Journal Vault")
st.caption("An objective soundboard for philosophical pondering and record keeping.")

client = genai.Client(api_key="AQ_Ab8RN6I2GVSuh661JYt7IFrhbzDs0bvyc0kXdslwZYwNMs8ayQ")

system_prompt = """
You are a private, objective intellectual journal record keeper and philosophical soundboard.
CRITICAL RULE 1: Do not affirm, validate, praise, or comment emotionally on what the user says. Do not offer sympathy or personal judgment. Remain entirely neutral.
CRITICAL RULE 2: Actively engage with the user's ideas through intellectual and philosophical pondering. If the user shares a concept, theory, or thought, you are encouraged to respond with objective analysis.
CRITICAL RULE 3: Ask sharp, clarifying, or thought-provoking questions whenever needed to help the user expand their record, unpack their reasoning, or dive deeper into their philosophical ideas. Keep your questions objective and curious, never leading or patronizing.
"""

if "chat" not in st.session_state:
    st.session_state.chat = client.chats.create(
        model="gemini-2.5-flash",
        config=types.GenerateContentConfig(system_instruction=system_prompt, temperature=0.5)
    )
if "history" not in st.session_state:
    st.session_state.history = []

for role, text in st.session_state.history:
    with st.chat_message(role):
        st.write(text)

if user_input := st.chat_input("Ponder out loud here..."):
    st.session_state.history.append(("user", user_input))
    with st.chat_message("user"):
        st.write(user_input)

    response = st.session_state.chat.send_message(user_input)
    st.session_state.history.append(("assistant", response.text))
    with st.chat_message("assistant"):
        st.write(response.text)