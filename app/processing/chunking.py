from transformers import AutoTokenizer

from langchain_text_splitters import (
    CharacterTextSplitter
)


def crear_chunks(documentos):

    tokenizer = AutoTokenizer.from_pretrained(
        "BAAI/bge-m3" # BAAI/bge-m3 para produccion
    )

    splitter = (
        CharacterTextSplitter
        .from_huggingface_tokenizer(
            tokenizer=tokenizer,
            chunk_size=1250,
            chunk_overlap=150
        )
    )

    chunks = splitter.split_documents(
        documentos
    )

    return chunks