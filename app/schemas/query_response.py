from dataclasses import dataclass, field


@dataclass(slots=True)
class QueryResponse:
    """
    Representa la respuesta final
    enviada a la interfaz.
    """

    answer: str

    sources: list[str] = field(
        default_factory=list
    )

    confidence: float | None = None

    success: bool = True