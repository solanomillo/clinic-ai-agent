"""
gemini.py

Responsabilidad:
    Crear y configurar el modelo Gemini.

Este módulo NO ejecuta consultas.
Solo construye el modelo.
"""

import logging

from langchain_google_genai import (
    ChatGoogleGenerativeAI
)

from app.config.settings import (
    settings
)

from app.core.exceptions import (
    ConfigurationError,
    LLMError
)

logger = logging.getLogger(__name__)


def cargar_llm() -> ChatGoogleGenerativeAI:
    """
    Construye una instancia configurada
    del modelo Gemini.

    Returns:
        ChatGoogleGenerativeAI
    """

    try:

        if not settings.GEMINI_API_KEY:
            raise ConfigurationError(
                "GEMINI_API_KEY no configurada."
            )

        logger.info(
            "Inicializando modelo Gemini: %s",
            settings.GEMINI_MODEL
        )

        llm = ChatGoogleGenerativeAI(
            model=settings.GEMINI_MODEL,
            temperature=settings.TEMPERATURE,
            google_api_key=settings.GEMINI_API_KEY
        )

        return llm

    except Exception as error:

        logger.exception(
            "Error al crear Gemini."
        )

        raise LLMError(
            "No fue posible inicializar Gemini."
        ) from error