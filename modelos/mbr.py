from __future__ import annotations

from typing import Optional, TYPE_CHECKING

if TYPE_CHECKING:
    from modelos.bus_datos import BusDatos


class Mbr:

    def __init__(self):
        self.__registro: str = ""
        self.__bus_datos: Optional[BusDatos] = None

    @property
    def registro(self):
        return self.__registro

    @registro.setter
    def registro(self, nuevo_valor):
        self.__registro = nuevo_valor

    @property
    def bus_datos(self):
        return self.__bus_datos

    @bus_datos.setter
    def bus_datos(self, bus_datos):
        self.__bus_datos = bus_datos

    def to_dict(self):
        return {
            "registro": self.__registro,
        }  