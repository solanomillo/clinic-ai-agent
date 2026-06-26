from langchain_core.prompts import (
    PromptTemplate
)

REWRITER_PROMPT = PromptTemplate.from_template(
    """
Genera una consulta optimizada para una búsqueda semántica en una base de conocimiento.

Debes devolver únicamente la consulta mejorada.

Pregunta del usuario:

{user_question}

Consulta optimizada:
"""
)