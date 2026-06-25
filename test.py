from app.services.rag_service import inicializar_rag


agent = inicializar_rag()

respuesta = agent.invoke(
    {
        "messages": [
            {
                "role": "user",
                "content": "¿Qué dice el documento sobre cancelar un turno?"
            }
        ]
    }
)

print(respuesta)
