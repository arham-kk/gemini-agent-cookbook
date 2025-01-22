import os
from dotenv import load_dotenv
from google import genai
from google.genai.types import GenerateContentConfig, Tool, GoogleSearch

load_dotenv()

GEMINI_API_KEY = os.getenv('GEMINI_API_KEY')

client = genai.Client(api_key=GEMINI_API_KEY)
model_id = "gemini-2.0-flash-exp"

#Helper function to make the code more concise
def generate_text(prompt, tools=None):
    config = GenerateContentConfig(tools=tools) if tools else None
    response = client.models.generate_content(model=model_id, contents=prompt, config=config)
    return response.text
