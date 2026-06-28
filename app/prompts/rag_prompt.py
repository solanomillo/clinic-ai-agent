from langchain_core.prompts import ChatPromptTemplate

RAG_PROMPT = ChatPromptTemplate.from_messages(
    [
        (
            "system",
            """
Eres un asistente especializado en responder únicamente con la información del contexto.

REGLAS:
- Usa solo el contexto.
- Si no está la información responde:
  "No encontré información en los documentos."

Contexto:
{contexto}
"""
        ),
        ("human", "{query}")
    ]
)