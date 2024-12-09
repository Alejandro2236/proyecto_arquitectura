from __future__ import annotations

from typing import Optional, TYPE_CHECKING

if TYPE_CHECKING:
    from modelos.bus_direcciones import BusDirecciones


class Mar:

    def __init__(self):
        self.__registro: str = ""
        self.__bus_direcciones: Optional[BusDirecciones] = None

    @property
    def registro(self):
        return self.__registro

    @registro.setter
    def registro(self, nuevo_valor):
        self.__registro = nuevo_valor
        self.__bus_direcciones.registro = nuevo_valor

    @property
    def bus_direcciones(self):
        raise AttributeError("Bus de direcciones no accesible desde afuera.")

    @bus_direcciones.setter
    def bus_direcciones(self, bus_direcciones):
        self.__bus_direcciones: BusDirecciones = bus_direcciones
