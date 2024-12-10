class BusControl:

    def __init__(self):
        self.__registro: str = ""

    @property
    def registro(self):
        return self.__registro

    @registro.setter
    def registro(self, nuevo_valor):
        self.__registro = nuevo_valor

    def to_dict(self):
        return {
            "registro": self.__registro,
        }  