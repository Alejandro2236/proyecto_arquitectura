class Pc:

    def __init__(self):
        self._registro: str = ""

    @property
    def registro(self):
        raise AttributeError("La señal de control no es accesible desde el exterior.")    

    @registro.setter
    def registro(self,registro: str):
        self._registro = registro

        