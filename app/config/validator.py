"""
validator.py

Valida configuraciones críticas antes de iniciar
la aplicación.
"""

from app.config.settings import settings

from app.core.exceptions import (
    ConfigurationError
)


def validar_configuracion() -> None:
    """
    Verifica que todas las variables críticas
    estén configuradas correctamente.
    """

    configuraciones_requeridas = {
        "GEMINI_API_KEY": settings.GEMINI_API_KEY,
        "COHERE_API_KEY": settings.COHERE_API_KEY,
    }

    faltantes = [
        nombre
        for nombre, valor
        in configuraciones_requeridas.items()
        if not valor
    ]

    if faltantes:
        raise ConfigurationError(
            "Variables de entorno faltantes: "
            + ", ".join(faltantes)
        )