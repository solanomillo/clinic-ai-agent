from langchain_huggingface import (
    HuggingFaceEmbeddings
)
from app.config.settings import settings

def cargar_embeddings():

    embeddings = HuggingFaceEmbeddings(
        model_name= settings.EMBEDDING_MODEL_DOS
    )

    return embeddings