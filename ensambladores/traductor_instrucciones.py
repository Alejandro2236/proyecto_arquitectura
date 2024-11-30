from controladores.controlador_unidad_control import ControladorUnidadControl
from utilidades import SeparadorPalabras


class TraductorInstrucciones:
    """
        Clase responsable de traducir un programa de lenguaje ensamblador a lenguaje de máquina.

        Esta clase **asume** que el programa ha sido previamente validado y que las instrucciones
        cumplen con la sintaxis esperada. La validación de la sintaxis debe realizarse por separado
        utilizando la clase ValidadorSintaxis.

        Cualquier error relacionado con la sintaxis (por ejemplo, un código de operación desconocido,
        una cantidad incorrecta de operandos, etc.) debe solucionarse antes de pasar el programa a
        este traductor.
        """

    def __init__(self, controlador_unidad_control: ControladorUnidadControl):
        self.__codops = controlador_unidad_control.obtener_codigos_binarios_codops()
        self.__tipos_dato = controlador_unidad_control.obtener_codigos_binarios_tipos_dato()

    def traducir_programa(self, instrucciones: list[str]) -> list[str]:
        """
        Traducir un programa de lenguaje ensamblador a lenguaje de máquina.

        :param instrucciones: Lista de instrucciones en lenguaje ensamblador válidas.
        :return: Lista de instrucciones en lenguaje de máquina traducidas.

        :raises ValueError: Si alguna instrucción no se puede traducir debido a un problema
                             que no ha sido capturado durante la validación (aunque se asume
                             que el programa ya ha sido validado).
        """

        if not instrucciones:
            raise ValueError("El programa debe tener al menos una instrucción.")

        programa_traducido = []

        for instruccion in instrucciones:
            if instruccion.strip() == "":
                continue
            instruccion_traducida: str = self.__traducir_instruccion(instruccion)
            programa_traducido.append(instruccion_traducida)

    def __traducir_instruccion(self, instruccion: str) -> str:
        if instruccion is None:
            raise ValueError("Debe pasar una instrucción para traducir.")
        palabras: list[str] = SeparadorPalabras.separar_palabras(instruccion, None)
        codop: str = palabras[0]
        operandos: list[str] = palabras[1:]
        codop_traducido: str = self.__traducir_codop(codop)
        lista_operandos_traducidos: list[str] = self.__traducir_operandos(operandos)
        operandos_traducidos_concatenados: str = "".join(lista_operandos_traducidos)
        instruccion_traducida: str = codop_traducido + operandos_traducidos_concatenados
        return instruccion_traducida

    def __traducir_codop(self, codop: str) -> str:
        raise NotImplementedError

    def __traducir_operandos(self, operandos: list[str]) -> list[str]:
        raise NotImplementedError
