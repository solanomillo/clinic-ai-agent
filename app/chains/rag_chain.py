from langchain_core.runnables import (
    RunnablePassthrough
)

from langchain_core.output_parsers import (
    StrOutputParser
)

from app.prompts.rag_prompt import (
    RAG_PROMPT
)


def crear_rag_chain(
    retriever,
    llm
):

    chain = (
        {
            "contexto":
                retriever,

            "query":
                RunnablePassthrough()
        }
        | RAG_PROMPT
        | llm
        | StrOutputParser()
    )

    return chain