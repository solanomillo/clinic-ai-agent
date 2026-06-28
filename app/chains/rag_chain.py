"""
rag_chain.py

Responsabilidad:
    Definir la cadena principal del RAG.
"""

from langchain_core.runnables import (
    RunnablePassthrough,
    RunnableParallel,
)

from langchain_core.output_parsers import (
    StrOutputParser,
)

from app.prompts.rag_prompt import (
    RAG_PROMPT,
)


def crear_rag_chain(
    retriever,
    llm,
):

    def format_docs(docs):
        """
        Convierte documentos en texto para el prompt.
        """
        return "\n\n".join(
            doc.page_content for doc in docs
        )

    chain = (
        RunnableParallel(
            {
                "contexto": retriever,
                "query": RunnablePassthrough(),
            }
        )
        | {
            "answer": (
                {
                    "contexto": lambda x: x["contexto"],
                    "query": lambda x: x["query"],
                }
                | RAG_PROMPT
                | llm
                | StrOutputParser()
            ),
            "documents": lambda x: x["contexto"],
        }
    )

    return chain