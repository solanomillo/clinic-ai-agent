def crear_retriever(
    vectorstore
):

    retriever = vectorstore.as_retriever(        
        search_type="mmr",  # MMR 
        search_kwargs={
            "k": 8,  # Recuperar 8 documentos
            "fetch_k": 20,  # Considerar 20 para diversificar
            "lambda_mult": 0.3  # Más diversidad (0 = máxima diversidad)
        }
    )

    return retriever