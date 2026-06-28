from app.services.vectorstore_service import (
    inicializar_vectorstore
)

from app.retrievers.retriever import (
    crear_retriever
)

from app.models.gemini import (
    cargar_llm
)

from app.chains.rag_chain import (
    crear_rag_chain
)


def inicializar_rag():

    vectorstore = (
        inicializar_vectorstore()
    )

    retriever = crear_retriever(
        vectorstore
    )

    llm = cargar_llm()

    rag_chain = crear_rag_chain(
        retriever,
        llm
    )

    return rag_chain