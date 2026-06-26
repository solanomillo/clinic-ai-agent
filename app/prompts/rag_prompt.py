from langchain_core.prompts import (
    ChatPromptTemplate
)

RAG_PROMPT = ChatPromptTemplate.from_messages(
    [
        (
            "system",
            """
Eres un asistente especializado en responder utilizando únicamente la información presente en el contexto.

Si la respuesta no se encuentra en el contexto, responde:

"No encontré información en los documentos."

Contexto:

{contexto}
"""
        ),
        (
            "human",
            "{query}"
        )
    ]
)