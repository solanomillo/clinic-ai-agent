"""
rag_agent.py

Agente principal del sistema RAG.
"""

import logging

from langchain.agents import (
    create_agent
)

logger = logging.getLogger(__name__)


def crear_rag_agent(
    llm,
    retrieval_tool
):
    """
    Construye el agente principal.
    """

    logger.info(
        "Creando agente RAG."
    )

    agent = create_agent(
        model=llm,
        tools=[retrieval_tool],
        system_prompt="""
Eres un asistente especializado en responder preguntas utilizando exclusivamente la documentación corporativa disponible.

Reglas obligatorias:

1. Utiliza la herramienta de búsqueda antes de responder.
2. Responde únicamente con información encontrada en los documentos.
3. Nunca inventes información.
4. Si no existe información suficiente, responde:

"No encontré información en los documentos disponibles."

5. Siempre indica:
   - documento utilizado
   - página utilizada

6. Resume la información de forma clara y profesional.

7. Si no existe información suficiente:
   - no adivines
   - no uses conocimiento externo
"""
    )

    return agent