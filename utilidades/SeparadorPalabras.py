from typing import Optional


def separar_palabras(instruccion: str, separador: Optional[str]) -> list[str]:
    """
    Separa una instrucción en palabras.

    :raises ValueError: Si la instrucción está vacía.
    """

    if not instruccion:
        raise ValueError("La instrucción no puede estar vacía.")
    if separador is None:
        return instruccion.split()
    return instruccion.split(separador)
