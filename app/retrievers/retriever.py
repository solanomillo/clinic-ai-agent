from app.config.settings import settings

def crear_retriever(
    vectorstore
):

    retriever = vectorstore.as_retriever(        
        search_type=settings.RETRIEVER_SEARCH_TYPE,  # MMR 
        search_kwargs={
            "k": settings.RETRIEVER_K,  # Recuperar 2 documentos
            "fetch_k": settings.RETRIEVER_FETCH_K,  # Considerar 15 para diversificar
            "lambda_mult": settings.RETRIEVER_LAMBDA_MULT  # Más diversidad (0 = máxima diversidad)
        }
    )

    return retriever