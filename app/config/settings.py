import os

from dotenv import load_dotenv

load_dotenv()


GEMINI_API_KEY = os.getenv(
    "GEMINI_API_KEY"
)

LANGSMITH_API_KEY = os.getenv(
    "LANGSMITH_API_KEY"
)

LANGSMITH_TRACING = os.getenv(
    "LANGSMITH_TRACING"
)

COHERE_API_KEY = os.getenv(
    "COHERE_API_KEY"
)