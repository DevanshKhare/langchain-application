import requests
import streamlit as st

def get_openai_response(input):
    response = requests.post(
        "http://localhost:8000/essay/invoke",
        json={"input": {"topic": input}}
    )
    return response.json()["output"]["content"]

st.title("AI Sensing")
input_text = st.text_input("Write an essay on the topic you want")

if input_text:
    st.write(get_openai_response(input_text))