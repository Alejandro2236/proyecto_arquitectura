from __future__ import annotations
from typing import TYPE_CHECKING, Optional

if TYPE_CHECKING:
    from modelos.mbr import Mbr

class BusDatos:

    def __init__(self):
        self.__registro: str = ""
        self.__mbr: Optional[Mbr] = None

    @property
    def registro(self):
        return self.__registro

    @registro.setter
    def registro(self, nuevo_valor):
        self.__registro = nuevo_valor

    @property
    def mbr(self):
        return self.__mbr

    @mbr.setter
    def mbr(self, mbr):
        self.__mbr: Mbr = mbr

    def enviar_a_mbr(self, dato: str):
        self.registro = dato
        self.__mbr.registro = dato

    def to_dict(self):
        return {
            "registro": self.__registro,
        }  