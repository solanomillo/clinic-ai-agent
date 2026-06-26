from langchain_core.output_parsers import (
    StrOutputParser
)

from app.prompts.rewriter_prompt import (
    REWRITER_PROMPT
)


def crear_query_rewriter(llm):

    chain = (
        REWRITER_PROMPT
        | llm
        | StrOutputParser()
    )

    return chain