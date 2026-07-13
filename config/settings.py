from dotenv import load_dotenv
import os

load_dotenv()

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
OPENAI_MODEL = os.getenv("OPENAI_MODEL", "gpt-5")

if not OPENAI_API_KEY:
    raise ValueError("A variável OPENAI_API_KEY não foi encontrada.")
