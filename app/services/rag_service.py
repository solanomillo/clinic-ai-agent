from app.services.vectorstore_service import (
    inicializar_vectorstore
)

from app.retrievers.retriever import (
    crear_retriever
)

from app.models.gemini import (
    cargar_llm
)

from app.models.cohere_model import (
    obtener_llm_cohere
) 

from app.chains.query_rewriter import (
    crear_query_rewriter
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
    llm_cohere = obtener_llm_cohere()

    rewriter = crear_query_rewriter(
        llm_cohere
    )

    rag_chain = crear_rag_chain(
        rewriter,
        retriever,
        llm
    )

    return rag_chain