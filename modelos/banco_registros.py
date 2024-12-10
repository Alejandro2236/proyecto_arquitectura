from modelos.registro import Registro


class BancoRegistros:

    def __init__(self):
        self.__registros: list[Registro] = []
        for _ in range(8):
            self.__registros.append(Registro())

    def obtener_registro(self, numero: int) -> Registro:
        return self.__registros[numero]
