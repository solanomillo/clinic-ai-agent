def crear_retriever(
    vectorstore
):

    retriever = vectorstore.as_retriever(        
        search_type="mmr",  # MMR 
        search_kwargs={
            "k": 3,  # Recuperar 2 documentos
            "fetch_k": 15,  # Considerar 15 para diversificar
            "lambda_mult": 0.3  # Más diversidad (0 = máxima diversidad)
        }
    )

    return retriever