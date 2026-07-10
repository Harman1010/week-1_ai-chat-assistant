from google import genai
from google.genai import types

from core.config import GEMINI_API_KEY,GEMINI_MODEL,SYSTEM_PROMPT

client = genai.Client(api_key=GEMINI_API_KEY)

def ask_ai(user_prompt:str)->str:
    try:
        response = client.models.generate_content(
        model = GEMINI_MODEL,
        contents = user_prompt,
        config = types.GenerateContentConfig(system_instruction=SYSTEM_PROMPT)
    )
        if response.text:
            return response.text
        return None
    except Exception as e:
        return f"Error : {e}"

