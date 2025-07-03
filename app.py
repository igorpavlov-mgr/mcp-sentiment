import json
import gradio as gr
from transformers import pipeline

# Load models (both CPU-friendly)
sentiment_classifier = pipeline("sentiment-analysis", model="distilbert-base-uncased-finetuned-sst-2-english")
sarcasm_classifier = pipeline("text-classification", model="helinivan/english-sarcasm-detector")

def analyze_text(text: str) -> str:
    """
    Analyze sentiment and detect sarcasm in the given text.

    Args:
        text (str): The text to analyze

    Returns:
        str: A JSON string with sentiment and sarcasm info
    """
    sentiment_result = sentiment_classifier(text)[0]
    sarcasm_result = sarcasm_classifier(text)[0]
    sarcasm_label = sarcasm_result["label"].lower()
    sarcasm_score = round(sarcasm_result["score"], 3)

    result = {
        "assessment": sentiment_result["label"].lower(),  # positive / negative
        "confidence": round(sentiment_result["score"], 3),
        "sarcasm_detected": sarcasm_label == "sarcasm" or sarcasm_score > 0.9,
        "sarcasm_confidence": sarcasm_score
    }

    return json.dumps(result)

demo = gr.Interface(
    fn=analyze_text,
    inputs=gr.Textbox(placeholder="Enter text to analyze..."),
    outputs=gr.Textbox(),
    title="Sentiment + Sarcasm Analyzer",
    description=(
        "This app performs sentiment analysis and sarcasm detection using CPU-compatible Hugging Face models. "
        "Integrated with Hugging Face's MCP (Multimodal Client Protocol) for seamless agent-to-app communication.\n\n"
        "⚙️ Models used:**\n\n"
        " • `distilbert-base-uncased-finetuned-sst-2-english` — sentiment analysis\n\n"
        " • `helinivan/english-sarcasm-detector` — sarcasm detection (fine-tuned BERT)\n\n"
        "🧾 Output format:**\n\n"
        " • `assessment`: Sentiment label (`\"positive\"` or `\"negative\"`)\n\n"
        " • `confidence`: Sentiment model's confidence score\n\n"
        " • `sarcasm_detected`: Boolean indicating if sarcasm was detected\n\n"
        " • `sarcasm_confidence`: Confidence score from sarcasm classifier\n\n"
        "🚩 Use the **Flag** button to report interesting or incorrect outputs (e.g., edge cases or sarcasm errors)."
    )
)


if __name__ == "__main__":
    demo.launch(mcp_server=True)
