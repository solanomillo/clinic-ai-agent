from langchain_core.prompts import (
    PromptTemplate
)

REWRITER_PROMPT = PromptTemplate.from_template(
    """
Eres un especialista en recuperación de información (Information Retrieval).

Tu tarea es reformular la consulta del usuario para maximizar la calidad de la búsqueda semántica.

Reglas:

1. Conserva la intención original.
2. Elimina palabras innecesarias.
3. Mantén nombres propios, fechas y términos técnicos.
4. No respondas la pregunta.
5. No inventes información.
6. Devuelve únicamente la consulta optimizada.

Consulta original:

{input}

Consulta optimizada:
"""
)