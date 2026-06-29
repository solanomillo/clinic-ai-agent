import os

from langchain_community.vectorstores import (
    FAISS
)
from app.config.settings import settings


FAISS_PATH = settings.VECTOR_DB_PATH


def crear_vectorstore(
    chunks,
    embeddings
):

    vectorstore = FAISS.from_documents(
        chunks,
        embeddings
    )

    return vectorstore


def guardar_vectorstore(
    vectorstore
):

    vectorstore.save_local(
        FAISS_PATH
    )


def cargar_vectorstore(
    embeddings
):

    return FAISS.load_local(
        FAISS_PATH,
        embeddings,
        allow_dangerous_deserialization=True
    )


def existe_vectorstore():

    return os.path.exists(
        FAISS_PATH
    )