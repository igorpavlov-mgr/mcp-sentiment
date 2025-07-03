Sentiment + Sarcasm Analyzer (Gradio + MCP)
This project is a lightweight Gradio application that performs sentiment analysis and sarcasm detection using Hugging Face Transformers. It is designed to run on CPU and was developed as part of the Hugging Face MCP Course. The app is fully compatible with the Hugging Face MCP server architecture.

## Live Demo
👉 [Launch the app on Hugging Face Spaces](https://huggingface.co/spaces/igorpavlov-mgr/mcp-sentiment)


Architecture Overview
Models (CPU-only):

- distilbert-base-uncased-finetuned-sst-2-english: Sentiment analysis
- helinivan/english-sarcasm-detector: Sarcasm detection

Frontend: Gradio UI

Backend: Python with Hugging Face Transformers

MCP Integration: Hugging Face MCP-compatible (gradio[mcp])

Features
- Sentiment classification: "positive" or "negative"
- Sarcasm detection with a probability score
- CPU-compatible (no GPU required)
- Simple and clean Gradio interface

Output Format
The app returns a structured JSON response with four fields:

json
Copy code
{
  "assessment": "positive",         // Sentiment: "positive" or "negative"
  "confidence": 1.0,                // Confidence score from sentiment model
  "sarcasm_detected": true,         // Whether sarcasm was detected
  "sarcasm_confidence": 0.97        // Confidence score from sarcasm model
}
Gradio Interface
The interface provides the following elements:

Element	Description
Textbox	Enter text to be analyzed
Submit	Run the sentiment and sarcasm analysis
Clear	Reset the input/output

Setup Instructions
1. Clone the repository
bash
Copy code
git clone https://github.com/YOUR_USERNAME/mcp-sentiment
cd mcp-sentiment
2. Create a virtual environment
bash
Copy code
python -m venv .venv

Then activate:
.venv\Scripts\activate      # Windows
source .venv/bin/activate   # macOS/Linux
3. Install dependencies
bash
Copy code
pip install -r requirements.txt
Ensure gradio[mcp] is included for MCP compatibility.

4. Add Hugging Face token
Create a .env file:

ini
Copy code
HF_TOKEN=your_token_here
5. Run the app locally
bash
Copy code
python app.py
Deploy to Hugging Face Spaces
bash
Copy code
git init
git remote add origin https://huggingface.co/spaces/YOUR_USERNAME/mcp-sentiment
git add .
git commit -m "Deploy MCP app"
git push -u origin main
Once pushed, the MCP server endpoint will be live on your Hugging Face Space.

Credits
Hugging Face MCP Course

Model: distilbert-base-uncased-finetuned-sst-2-english

Model: helinivan/english-sarcasm-detector

Gradio
