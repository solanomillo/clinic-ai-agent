"""
chunking.py

Responsabilidad:
    Dividir documentos en chunks
    optimizados para embeddings.
"""

import logging

from transformers import (
    AutoTokenizer
)

from langchain_text_splitters import (
    RecursiveCharacterTextSplitter
)

from langchain_core.documents import (
    Document
)

from app.config.settings import (
    settings
)

from datetime import datetime

logger = logging.getLogger(__name__)


def crear_chunks(
    documentos: list[Document]
) -> list[Document]:
    """
    Divide documentos en fragmentos.

    Args:
        documentos:
            Documentos limpios.

    Returns:
        Chunks listos para embeddings.
    """

    tokenizer = (
        AutoTokenizer.from_pretrained(
            settings.EMBEDDING_MODEL
        )
    )

    splitter = (
        RecursiveCharacterTextSplitter
        .from_huggingface_tokenizer(
            tokenizer=tokenizer,
            chunk_size=settings.CHUNK_SIZE,
            chunk_overlap=settings.CHUNK_OVERLAP
        )
    )

    chunks = splitter.split_documents(
        documentos
    )
    
    fecha_ingesta = (
    datetime.now()
    .strftime("%Y-%m-%d")
    )

    for indice, chunk in enumerate(chunks):

        source = (
            chunk.metadata.get(
                "source",
                "desconocido"
            )
        )

        page = (
            chunk.metadata.get(
                "page",
                0
            )
        )

        nombre_documento = (
            source.split("/")[-1]
        )

        chunk.metadata.update(
            {
                "chunk_id":
                    f"{nombre_documento}_{page}_{indice}",

                "document_name":
                    nombre_documento,

                "fecha_ingesta":
                    fecha_ingesta,

                "categoria":
                    "general"
            }
        )

    logger.info(
        "Chunks generados: %s",
        len(chunks)
    )

    return chunks