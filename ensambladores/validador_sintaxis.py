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
        if not instruccion:
            raise ValueError("Para separar una instrucción en palabras no puede estar vacia")
        return instruccion.split()

    def __validar_codop(self, codop: str):
        if codop not in self.__obtener_nombres_codop():
            raise ValueError(f"Código de operación '{codop}' desconocido")

    def __obtener_nombres_codop(self) -> list[str]:
        return [codop["nombre"] for codop in self.__codops_info]

    def __validar_cantidad_operandos(self, codop: str, operandos: list[str]):
        cantidad_operandos_esperados: int = self.__obtener_cantidad_operandos_codop(codop)

        if len(operandos) != cantidad_operandos_esperados:
            raise ValueError(
                f"La instrucción con código de operación '{codop}' espera {cantidad_operandos_esperados}"
                f" operandos, pero se proporcionaron {len(operandos)}."
            )

    def __obtener_cantidad_operandos_codop(self, codop: str) -> int:
        for codop_info in self.__codops_info:
            if codop_info["nombre"] == codop:
                return codop_info["cantidad_operandos"]

        raise ValueError(f"Código de operación '{codop}' desconocido")
