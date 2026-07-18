from google import genai
from config import GEMINI_API_KEY

client = genai.Client(api_key=GEMINI_API_KEY)

for model in client.models.list():
    if hasattr(model, "supported_actions"):
        if "generateContent" in model.supported_actions:
            print(model.name)