"""
settings.py

Configuración centralizada de la aplicación.

Responsabilidades:
- Cargar variables de entorno.
- Validar configuraciones críticas.
- Exponer parámetros globales.
"""

from __future__ import annotations

import os

from dotenv import load_dotenv

load_dotenv()


class Settings:
    """
    Configuración global de la aplicación.
    """

    # =========================
    # API KEYS
    # =========================

    GEMINI_API_KEY: str | None = os.getenv(
        "GEMINI_API_KEY"
    )

    COHERE_API_KEY: str | None = os.getenv(
        "COHERE_API_KEY"
    )

    LANGSMITH_API_KEY: str | None = os.getenv(
        "LANGSMITH_API_KEY"
    )

    # =========================
    # LANGSMITH
    # =========================

    LANGSMITH_TRACING: bool = (
        os.getenv(
            "LANGSMITH_TRACING",
            "false"
        ).lower()
        == "true"
    )

    # =========================
    # MODELOS
    # =========================

    GEMINI_MODEL: str = (
        "gemini-2.5-flash"
    )

    COHERE_MODEL: str = (
        "command-a-plus-05-2026"
    )

    TEMPERATURE: float = 0.0

    # =========================
    # EMBEDDINGS
    # =========================

    EMBEDDING_MODEL: str = (
        "BAAI/bge-m3"
    )
    
    EMBEDDING_MODEL_DOS: str = (
        "all-MiniLM-L6-v2"
    )

    # =========================
    # CHUNKING
    # =========================

    CHUNK_SIZE: int = 1250

    CHUNK_OVERLAP: int = 150

    # =========================
    # VECTOR STORE
    # =========================

    VECTOR_DB_PATH: str = (
        "./vector_db/faiss_index"
    )

    DOCUMENTS_PATH: str = (
        "./data/documentos"
    )

    # =========================
    # RETRIES
    # =========================

    MAX_RETRIES: int = 3

    RETRY_DELAY_SECONDS: int = 5
    
    RETRIEVER_SEARCH_TYPE: str = "mmr"

    RETRIEVER_K: int = 8

    RETRIEVER_FETCH_K: int = 20

    RETRIEVER_LAMBDA_MULT: float = 0.3
    
    # =========================
    # OCR
    # =========================

    OCR_LANGUAGE: str = "spa"


settings = Settings()