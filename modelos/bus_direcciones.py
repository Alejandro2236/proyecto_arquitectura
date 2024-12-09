from typing import Optional, TYPE_CHECKING

if TYPE_CHECKING:
    from modelos.mar import Mar


class BusDirecciones:

    def __init__(self):
        self.__registro: str = ""
        self.__mar: Optional[Mar] = None

    @property
    def registro(self):
        return self.__registro

    @registro.setter
    def registro(self, nuevo_valor):
        self.__registro = nuevo_valor

    @property
    def mar(self):
        raise AttributeError("Bus de direcciones no accesible desde afuera.")

    @mar.setter
    def mar(self, mar):
        self.__mar: Mar = mar
