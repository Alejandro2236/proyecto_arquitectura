from typing import Optional, TYPE_CHECKING

if TYPE_CHECKING:
    from modelos.mar import Mar


class BusDirecciones:

    def __init__(self):
        self.__registro: str = ""
        self.__mar: Optional[Mar] = None

    @property
    def mar(self):
        raise AttributeError("Bus de direcciones no accesible desde afuera.")

    @mar.setter
    def mar(self, mar):
        self.__mar: Mar = mar
