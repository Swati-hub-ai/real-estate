# PropertyBot: AI-Powered Real Estate Assistant

**PropertyBot** is a smart, multi-agent chatbot that understands both property issues from images and tenancy law questions—like a virtual landlord and property inspector in one.

---

## How It Works

### Ask Any Rental or Property Question
- "Can my landlord increase rent midway?"
- "What if they don't return my deposit?"

### Upload Property Issue Photos
- Upload any image showing a property issue.
- The bot diagnoses the issue and gives helpful advice.

### Smart Routing
- PropertyLoop automatically detects whether your question is legal or visual.
- It routes the question to the correct AI agent.

---

## Agents Used

### Agent 1: Property Issue Detector (Image + Text)
- Accepts uploaded images of property issues.
- Uses **BLIP** to describe the image (e.g., “black mold near ceiling”).
- Sends that description to **Mistral via Ollama** to get actionable suggestions.

### Agent 2: Tenancy FAQ Bot (Text)
- Handles all tenancy law queries.
- Provides human-like answers using **Ollama + Mistral**.
- Adapts responses based on user location (e.g., "London", "New York").

---

## Technologies Used

| Component        | Tech Stack                        |
|------------------|-----------------------------------|
| Chatbot UI       | Streamlit                         |
| Image Captioning | Hugging Face BLIP                 |
| Local LLM        | Huggingface running via Zapyer    |
| Routing          | Custom rule-based logic           |
| Offline Ready    | Runs 100% locally (no API keys!)  |

---

## Real-Life Examples

**Example 1: Image-Based Property Issue**

- User uploads image of cracked paint and asks:  
  _“What’s wrong with this wall?”_

  > **Agent 1 replies**: “This appears to be paint peeling due to moisture. Consider checking for leaks and using anti-damp paint.”

**Example 2: Text-Based Legal Query**

- User types:  
  _“Can my landlord evict me without notice in New York?”_

  > **Agent 2 replies**: “In New York, landlords must give written notice unless there’s a violation of lease terms. Emergency evictions require court action.”

---

## How To Get Started

```bash
# Clone the repo
git clone https://github.com/Swati-hub-ai/real-estate
