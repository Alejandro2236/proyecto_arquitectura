class Mar:

    def __init__(self):
        self.__registro: str = ""

    @property
    def registro(self):
        return self.__registro

    @registro.setter
    def registro(self, nuevo_valor):
        self.__registro = nuevo_valor
