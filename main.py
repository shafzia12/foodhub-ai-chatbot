import streamlit as st
from chatbot import get_response
from guardrails import validate_input

st.set_page_config(page_title="FoodHub AI", layout="wide")

st.title("🍔 FoodHub AI Customer Support")

if "history" not in st.session_state:
    st.session_state.history = []

for role, msg in st.session_state.history:
    with st.chat_message(role):
        st.write(msg)

user_input = st.chat_input("Ask about your order...")

if user_input:
    st.session_state.history.append(("user", user_input))

    with st.chat_message("user"):
        st.write(user_input)

    # Guardrails
    blocked = validate_input(user_input)
    if blocked:
        response = blocked
    else:
        response = get_response(user_input)

    st.session_state.history.append(("assistant", response))

    with st.chat_message("assistant"):
        st.write(response)