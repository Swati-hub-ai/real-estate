from transformers import BlipProcessor, BlipForConditionalGeneration
from huggingface_hub import InferenceClient
from PIL import Image
import torch
import os

# Load BLIP for image captioning
blip_processor = BlipProcessor.from_pretrained("Salesforce/blip-image-captioning-base", use_fast=True)
blip_model = BlipForConditionalGeneration.from_pretrained("Salesforce/blip-image-captioning-base")

# Load Hugging Face Inference Client for LLM
HF_TOKEN = os.getenv("HUGGINGFACEHUB_API_TOKEN")
llm_client = InferenceClient(model="mistralai/Mistral-7B-Instruct-v0.3", token=HF_TOKEN)

# Get image caption using BLIP
def get_image_description(image_path):
    image = Image.open(image_path).convert('RGB')
    inputs = blip_processor(image, return_tensors="pt")
    with torch.no_grad():
        out = blip_model.generate(**inputs)
    caption = blip_processor.decode(out[0], skip_special_tokens=True)
    return caption

# Send caption to LLM for troubleshooting advice
def get_troubleshooting_suggestion(caption):
    prompt = f"""You are a helpful assistant diagnosing property issues.
Image Description: "{caption}"
Give a helpful, actionable suggestion to fix or inspect the issue in detail."""

    response = llm_client.text_generation(prompt, max_new_tokens=500, temperature=0.7)
    return response.strip()

# Combine into one agent function
def agent1_flow(image_path):
    caption = get_image_description(image_path)
    suggestion = get_troubleshooting_suggestion(caption)
    return caption, suggestion
