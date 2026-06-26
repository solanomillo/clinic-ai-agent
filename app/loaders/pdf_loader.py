from langchain_community.document_loaders import (
    DirectoryLoader,
    PyPDFLoader
)


def cargar_documentos():

    loader = DirectoryLoader(
        "./data/documentos",
        glob="*.pdf",
        loader_cls=PyPDFLoader
    )

    documentos = loader.load()

    return documentos