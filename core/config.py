from dotenv import load_dotenv
import os

load_dotenv()


GEMINI_API_KEY=os.getenv("GEMINI_API_KEY")

if not GEMINI_API_KEY:
    raise ValueError("Gemini API Key was not found")

GEMINI_MODEL="gemini-2.5-flash"

SYSTEM_PROMPT = """

You are an expert chatbot.

Answer the user's query in natural language.

Rules:
If the answer is not known , clearly state "Answer not known"
If the answer is unethical , clearly refuse to answer.


"""