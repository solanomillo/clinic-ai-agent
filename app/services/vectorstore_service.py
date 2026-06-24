from app.loaders.pdf_loader import (
    cargar_documentos
)

from app.processing.chunking import (
    crear_chunks
)

from app.processing.embeddings import (
    cargar_embeddings
)

from app.vectorstores.faiss_store import (
    crear_vectorstore,
    guardar_vectorstore,
    cargar_vectorstore,
    existe_vectorstore
)


def inicializar_vectorstore():

    embeddings = cargar_embeddings()

    if existe_vectorstore():

        print(
            "Cargando índice FAISS..."
        )

        return cargar_vectorstore(
            embeddings
        )

    print(
        "Creando índice FAISS..."
    )

    documentos = cargar_documentos()

    chunks = crear_chunks(
        documentos
    )

    vectorstore = crear_vectorstore(
        chunks,
        embeddings
    )

    guardar_vectorstore(
        vectorstore
    )

    return vectorstore