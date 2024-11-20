class ValidadorSintaxis:
    def __init__(self, codops_info: dict):
        self.__codops_info: list[dict] = list(codops_info.values())

    def validar_programa(self, instrucciones: list[str]) -> bool:
        if not instrucciones:
            raise ValueError("El programa debe tener al menos una instrucción.")
        for instruccion in instrucciones:
            self.__validar_instruccion(instruccion)
        return True

    def __validar_instruccion(self, instruccion: str):
        palabras = self.__separar_palabras(instruccion)
        codop: str = palabras[0]
        operandos: list[str] = palabras[1:]
        self.__validar_codop(codop)
        self.__validar_cantidad_operandos(codop, operandos)

    def __separar_palabras(self, instruccion: str) -> list[str]:
        raise NotImplementedError

    def __validar_codop(self, codop: str):
        raise NotImplementedError

    def __validar_cantidad_operandos(self, codop: str, operandos: list[str]):
        raise NotImplementedError
