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
        raise NotImplementedError
