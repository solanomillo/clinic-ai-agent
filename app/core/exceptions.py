"""
Excepciones personalizadas de la aplicación.

Permiten desacoplar errores internos
de los mensajes mostrados al usuario.
"""


class AppException(Exception):
    """
    Excepción base del proyecto.
    """
    pass


class ConfigurationError(AppException):
    """
    Error de configuración.
    """
    pass


class VectorStoreError(AppException):
    """
    Error relacionado con FAISS.
    """
    pass


class DocumentLoadError(AppException):
    """
    Error durante la carga documental.
    """
    pass


class EmbeddingError(AppException):
    """
    Error al generar embeddings.
    """
    pass


class LLMError(AppException):
    """
    Error general de modelos LLM.
    """
    pass


class RateLimitError(LLMError):
    """
    Error 429.
    """
    pass