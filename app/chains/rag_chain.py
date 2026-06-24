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
    rewriter,
    retriever,
    llm
):

    chain = (
        {
            "contexto":
                rewriter | retriever,

            "query":
                RunnablePassthrough()
        }
        | RAG_PROMPT
        | llm
        | StrOutputParser()
    )

    return chain