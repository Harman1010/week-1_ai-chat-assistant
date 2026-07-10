from dotenv import load_dotenv
import os

load_dotenv()


GEMINI_API_KEY=os.getenv("GEMINI_API_KEY")

if not GEMINI_API_KEY:
    raise ValueError("Gemini API Key was not found")

GEMINI_MODEL="gemini-2.5-flash"