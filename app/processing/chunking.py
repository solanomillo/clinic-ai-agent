from transformers import AutoTokenizer

from langchain_text_splitters import (
    RecursiveCharacterTextSplitter
)
from app.config.settings import settings


def crear_chunks(documentos):

    tokenizer = AutoTokenizer.from_pretrained(
        settings.CHUNKS_MODEL_TOKENIZER
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

    return chunks