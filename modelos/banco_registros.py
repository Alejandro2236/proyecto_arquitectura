from modelos.registro import Registro


class BancoRegistros:

    def __init__(self):
        self.__registros: list[Registro] = []

    def to_dict(self):
        return {
            "registros": self.__registros,
        }  