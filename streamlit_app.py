import streamlit as st
from src.chatbot import HealthChatbot

# Load the chatbot
chatbot = HealthChatbot(
    vector_db_path="vector_db",
    model_name="gpt-3.5-turbo", 
    prompt_type="basic"
)

st.title("Health Management Chatbot")

query = st.text_input("Enter your health question:")
patient_id = st.text_input("Patient ID (optional):")

if st.button("Ask"):
    with st.spinner("Processing..."):
        response = chatbot.get_answer(query, patient_id if patient_id else None)
        st.markdown(f"**Response:**\n\n{response}")