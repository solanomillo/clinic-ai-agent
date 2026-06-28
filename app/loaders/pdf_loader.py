"""
pdf_loader.py

Responsabilidad:
    Cargar todos los documentos PDF disponibles de forma
    recursiva desde el directorio configurado.
"""

from langchain_community.document_loaders import (
    DirectoryLoader,
    PyPDFLoader,
)


def cargar_documentos():
    """
    Carga todos los documentos PDF ubicados dentro del directorio
    de documentos y sus subdirectorios.

    Returns:
        list[Document]: Lista de documentos cargados.
    """

    loader = DirectoryLoader(
        path="./data/documentos",
        glob="**/*.pdf",
        loader_cls=PyPDFLoader,
    )

    return loader.load()