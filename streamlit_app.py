import streamlit as st
from agent1 import agent1_flow  # Your function to process image and return (caption, suggestion)
from agent2 import ask_tenancy_faq  # Your text-based agent
from router import route_message

st.set_page_config(page_title="PropertyLoop Assistant", layout="centered")
st.title("🏡 PropertyLoop Multi-Agent Assistant")

st.markdown("Upload an image or ask a question related to property or tenancy.")

# Input area
uploaded_image = st.file_uploader("📤 Upload Property Image (Optional)", type=["jpg", "jpeg", "png"])
user_text = st.text_input("💬 Ask your question (Optional)")
location = st.text_input("🌍 Enter your location (Optional)")

if st.button("🚀 Get Response"):
    # Routing decision
    route = route_message(user_text, has_image=uploaded_image is not None)

    if route == "agent1":
        with open("temp_image.jpg", "wb") as f:
            f.write(uploaded_image.read())
        caption, suggestion = agent1_flow("temp_image.jpg")
        st.markdown(f"### 🖼️ Issue Description:\n> {caption}")
        st.markdown(f"### 🛠️ Troubleshooting Suggestion:\n> {suggestion}")

    elif route == "agent2":
        response = ask_tenancy_faq(user_text, location=location)
        st.markdown(f"### 📜 Tenancy Answer:\n> {response}")

    elif route == "clarify":
        st.warning("❓ Please clarify: Are you reporting a property issue or asking a tenancy-related question?")
