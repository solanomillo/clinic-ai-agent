from langchain_huggingface import (
    HuggingFaceEmbeddings
)


def cargar_embeddings():

    embeddings = HuggingFaceEmbeddings(
        model_name="all-MiniLM-L6-v2" # BAAI/bge-m3 para produccion
    )

    return embeddings