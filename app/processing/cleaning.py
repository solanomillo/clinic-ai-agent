"""
cleaning.py

Responsabilidad:
    Centralizar el proceso de limpieza de documentos antes de la
    generación de chunks.

    En esta primera versión la función actúa como un passthrough.
    En los siguientes commits se incorporarán reglas de limpieza
    como eliminación de encabezados, pies de página, espacios
    duplicados y caracteres no deseados.
"""

from langchain_core.documents import Document


def limpiar_documentos(
    documentos: list[Document],
) -> list[Document]:
    """
    Ejecuta el pipeline de limpieza de documentos.

    Actualmente no modifica el contenido y devuelve los documentos
    originales. Se implementará progresivamente en los siguientes
    commits.

    Args:
        documentos: Lista de documentos cargados.

    Returns:
        Lista de documentos lista para continuar con el pipeline.
    """

    return documentos