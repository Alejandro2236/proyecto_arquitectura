class Pc:

    def __init__(self):
        self.__registro: str = ""

    @property
    def registro(self):
        raise AttributeError("La señal de control no es accesible desde el exterior.")    

    @registro.setter
    def registro(self,registro: str):
        self.__registro = registro

        