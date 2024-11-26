from typing import Optional

from controladores.controlador_unidad_control import ControladorUnidadControl


class ValidadorSintaxis:
    def __init__(self, controlador_unidad_control: ControladorUnidadControl):
        self.__info_codops: list[dict] = controlador_unidad_control.obtener_cantidad_operandos_codops()
        self.__nombres_codops: set[str] = controlador_unidad_control.obtener_nombres_codop()
        self.__etiquetas: Optional[list] = None

    def validar_programa(self, instrucciones: list[str]) -> bool:
        """
        Valida la sintaxis de un programa de ensamblador reducido a partir de una lista de instrucciones.

        :param instrucciones: Lista de instrucciones en formato de texto.
        :type instrucciones: list
        :return: True si todas las instrucciones son válidas.
        :raises ValueError: Si alguna instrucción es inválida.
        """

        if not instrucciones:
            raise ValueError("El programa debe tener al menos una instrucción.")
        for linea, instruccion in enumerate(instrucciones, start=1):
            self.__validar_instruccion(instruccion, linea)
        return True

    def __validar_instruccion(self, instruccion: str, linea: int):
        """
        Valida una única instrucción dentro del programa, verificando el código de operación
        y la cantidad correcta de operandos.

        :param instruccion: La instrucción a validar.
        :type instruccion: str
        :param linea: El número de línea en el programa (para reportar errores).
        :type linea: int
        :raises ValueError: Si la instrucción es inválida.
        """

        palabras = self.__separar_palabras(instruccion)
        if self.__es_etiqueta(palabras, linea):
            self.__etiquetas.append(palabras[0][:-1])
            return
        codop: str = palabras[0]
        operandos: list[str] = palabras[1:]

        self.__validar_codop(codop, linea)
        self.__validar_cantidad_operandos(codop, operandos, linea)

    @staticmethod
    def __separar_palabras(instruccion: str) -> list[str]:
        """
            Separa una instrucción en sus componentes de palabras (código de operación y operandos).

            :param instruccion: La instrucción a separar.
            :type instruccion: str
            :return: Lista de palabras que componen la instrucción.
            :raises ValueError: Si la instrucción está vacía.
            """

        if not instruccion:
            raise ValueError("La instrucción no puede estar vacía.")
        return instruccion.split()

    def __es_etiqueta(self, palabras_instruccion: list[str], linea: int) -> bool:
        if len(palabras_instruccion) != 1:
            return False
        etiqueta: str = palabras_instruccion[0]
        self.__validar_etiqueta(etiqueta, linea)

    def __validar_etiqueta(self, etiqueta: str, linea: int):
        if etiqueta[-1] != ":":
            raise ValueError(f"La etiqueta {etiqueta} de la línea {linea} debe terminar con ':'")

        nombre_etiqueta: str = etiqueta[:-1]
        if nombre_etiqueta is None or nombre_etiqueta == "":
            raise ValueError(f"La etiqueta en la línea {linea} debe tener nombre.")

        if nombre_etiqueta in self.__etiquetas:
            raise ValueError(f"La etiqueta {nombre_etiqueta} de la línea {linea} ya existe.")

    def __validar_codop(self, codop: str, linea: int):
        if codop not in self.__nombres_codops:
            raise ValueError(f"Código de operación '{codop}' desconocido en la línea {linea}")

    def __validar_cantidad_operandos(self, codop: str, operandos: list[str], linea: int):
        """
        Verifica que la cantidad de operandos proporcionada coincida con la cantidad esperada
        para un código de operación dado.

        :param codop: El código de operación que se está validando.
        :type codop: str
        :param operandos: Los operandos proporcionados en la instrucción.
        :type operandos: list
        :param linea: La línea del programa donde se encuentra la instrucción.
        :type linea: int
        :raises ValueError: Si el número de operandos es incorrecto.
        """

        cantidad_operandos_esperados: int = self.__obtener_cantidad_operandos_codop(codop)

        if len(operandos) != cantidad_operandos_esperados:
            raise ValueError(
                f"La instrucción con código de operación '{codop}' en la línea {linea} espera "
                f"{cantidad_operandos_esperados} operandos, pero se proporcionaron {len(operandos)}."
            )

    def __obtener_cantidad_operandos_codop(self, codop: str) -> int:
        for codop_info in self.__info_codops:
            if codop_info["nombre"] == codop:
                return codop_info["cantidad_operandos"]

        raise ValueError(f"Código de operación '{codop}' desconocido")
