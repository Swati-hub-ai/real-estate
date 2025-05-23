from huggingface_hub import InferenceClient
import os
import streamlit as st

# agent1.py or agent2.py
HF_TOKEN = os.getenv("HUGGINGFACEHUB_API_TOKEN") or st.secrets["HUGGINGFACEHUB_API_TOKEN"]

llm_client = InferenceClient(model="HuggingFaceH4/zephyr-7b-beta", token=HF_TOKEN)

def ask_tenancy_faq(question, location=None):
    prompt = f"""You are a legal assistant that helps renters understand tenancy laws, rental agreements, landlord responsibilities, and deposit issues.

Question: {question}
Location: {location if location else 'Not specified'}

Respond clearly and helpfully, considering the location if provided."""

    response = llm_client.text_generation(prompt, max_new_tokens=500, temperature=0.7)
    return response.strip()
