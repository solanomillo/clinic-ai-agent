"""
cleaning.py

Responsabilidad:
    Limpiar y normalizar el contenido de los documentos antes de
    generar los chunks para el índice vectorial.
"""

from __future__ import annotations

import re

from langchain_core.documents import Document


def limpiar_documentos(
    documentos: list[Document],
) -> list[Document]:
    """
    Limpia y normaliza una colección de documentos.

    Acciones realizadas:
        - Elimina caracteres invisibles.
        - Normaliza saltos de línea.
        - Elimina espacios duplicados.
        - Elimina líneas vacías.
        - Elimina tabulaciones.

    Args:
        documentos: Lista de documentos cargados.

    Returns:
        Lista de documentos limpios.
    """

    documentos_limpios: list[Document] = []

    for documento in documentos:

        contenido = _limpiar_texto(
            documento.page_content
        )

        documentos_limpios.append(
            Document(
                page_content=contenido,
                metadata=documento.metadata.copy()
            )
        )

    return documentos_limpios


def _limpiar_texto(
    texto: str,
) -> str:
    """
    Aplica reglas básicas de limpieza al texto.

    Args:
        texto: Texto original.

    Returns:
        Texto limpio y normalizado.
    """

    # Eliminar caracteres invisibles frecuentes
    texto = texto.replace("\ufeff", "")
    texto = texto.replace("\u200b", "")
    texto = texto.replace("\xa0", " ")

    # Normalizar saltos de línea
    texto = texto.replace("\r\n", "\n")
    texto = texto.replace("\r", "\n")

    # Reemplazar tabulaciones
    texto = texto.replace("\t", " ")

    # Eliminar espacios repetidos
    texto = re.sub(
        r"[ ]{2,}",
        " ",
        texto
    )

    # Eliminar líneas vacías repetidas
    texto = re.sub(
        r"\n{3,}",
        "\n\n",
        texto
    )

    # Eliminar espacios al inicio y final de cada línea
    lineas = [
        linea.strip()
        for linea in texto.split("\n")
    ]

    # Eliminar líneas completamente vacías
    lineas = [
        linea
        for linea in lineas
        if linea
    ]

    return "\n".join(lineas).strip()