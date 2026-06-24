from langchain_cohere import ChatCohere
from langchain_core.messages import HumanMessage
from app.config import settings


def obtener_llm_cohere():
    llm = ChatCohere(
        model="command-a-plus-05-2026",
        cohere_api_key = settings.COHERE_API_KEY
    )
    return llm
