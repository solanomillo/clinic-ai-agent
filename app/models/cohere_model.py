"""
cohere_model.py

Responsabilidad:
    Crear y configurar el modelo Cohere.

Se utiliza para reescritura de consultas.
"""

import logging

from langchain_cohere import (
    ChatCohere
)

from app.config.settings import (
    settings
)

from app.core.exceptions import (
    ConfigurationError,
    LLMError
)

logger = logging.getLogger(__name__)


def obtener_llm_cohere() -> ChatCohere:
    """
    Construye una instancia configurada
    de Cohere.

    Returns:
        ChatCohere
    """

    try:

        if not settings.COHERE_API_KEY:
            raise ConfigurationError(
                "COHERE_API_KEY no configurada."
            )

        logger.info(
            "Inicializando modelo Cohere: %s",
            settings.COHERE_MODEL
        )

        llm = ChatCohere(
            model=settings.COHERE_MODEL,
            cohere_api_key=settings.COHERE_API_KEY
        )

        return llm

    except Exception as error:

        logger.exception(
            "Error al crear Cohere."
        )

        raise LLMError(
            "No fue posible inicializar Cohere."
        ) from error