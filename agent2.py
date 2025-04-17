from huggingface_hub import InferenceClient
import os

HF_TOKEN = os.getenv("HUGGINGFACEHUB_API_TOKEN") 
llm_client = InferenceClient(model="mistralai/Mistral-7B-Instruct-v0.3", token=HF_TOKEN)

def ask_tenancy_faq(question, location=None):
    prompt = f"""You are a legal assistant that helps renters understand tenancy laws, rental agreements, landlord responsibilities, and deposit issues.

Question: {question}
Location: {location if location else 'Not specified'}

Respond clearly and helpfully, considering the location if provided."""

    response = llm_client.text_generation(prompt, max_new_tokens=500, temperature=0.7)
    return response.strip()
