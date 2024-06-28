import streamlit as st
import os
from streamlit_option_menu import option_menu
import google.generativeai as genai
import json

# Load API key from config.json
working_directory = os.path.dirname(os.path.abspath(__file__))
config_file_path = f"{working_directory}/config.json"
config_data = json.load(open(config_file_path))

apikey = config_data["Google_API_KEY"]

# Configure API key
genai.configure(api_key=apikey)

# Define the model ID you want to use
MODEL_ID = " models/gemini-1.5-pro-001"

st.set_page_config(
    page_title="BOT JI",
    page_icon="🧠",
    layout="centered"
)

with st.sidebar:
    selected = option_menu(
        menu_title="Bot Guru",
        options=["ChatBot", "Image Analysing", "Ask me anything"],
        menu_icon='robot',
        icons=['chat-dots', 'image-fill', 'patch-question'],
        default_index=0
    )

if selected == "ChatBot":

    st.title("🤖 ChatBot")

    user_prompt = st.chat_input("Ask Gemini Pro...")

    if user_prompt:
        st.chat_message("user").markdown(user_prompt)

        try:
            # Generate content using the model
            gemini_response = genai.generate_text(
                model=MODEL_ID,
                prompt=user_prompt,
                temperature=0.7,
                max_output_tokens=150
            )

            st.write(f"Gemini Response: {gemini_response}")

            if gemini_response and 'candidates' in gemini_response:
                response_text = gemini_response['candidates'][0]['output']
                with st.chat_message("assistant"):
                    st.markdown(response_text)
            else:
                st.write("No response received from the model.")
        except Exception as e:
            st.write(f"Error: {e}")
