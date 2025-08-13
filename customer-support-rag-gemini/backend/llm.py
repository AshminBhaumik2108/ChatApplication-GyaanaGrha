from langchain_google_genai import GoogleGenerativeAI
from backend import config

def get_llm(temperature=None):
    # Allow dynamic temperature override
    temp = temperature if temperature is not None else config.TEMPERATURE
    return GoogleGenerativeAI(
        model=config.GEMINI_MODEL,
        google_api_key=config.GOOGLE_API_KEY,
        temperature=temp,
        max_output_tokens=config.MAX_TOKENS
    )
