class Pc:

    def __init__(self):
        self.__registro: str = "0" * 8

    @property
    def registro(self):
        return self.__registro

    @registro.setter
    def registro(self,registro: str):
        self.__registro = registro

        