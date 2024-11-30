from controladores.controlador_unidad_control import ControladorUnidadControl
from utilidades import SeparadorPalabras


class ValidadorSintaxis:
    def __init__(self, controlador_unidad_control: ControladorUnidadControl):
        """
        Inicializa el validador de sintaxis con información sobre códigos de operación
        y prepara una lista para registrar etiquetas del programa.

        :param controlador_unidad_control: Controlador para obtener datos del conjunto de instrucciones.
        :type controlador_unidad_control: ControladorUnidadControl
        """

        self.__info_codops: list[dict] = controlador_unidad_control.obtener_cantidad_operandos_codops()
        self.__nombres_codops: set[str] = controlador_unidad_control.obtener_nombres_codop()
        self.__etiquetas: list = []

    def validar_programa(self, instrucciones: list[str]) -> bool:
        """
        Valida un programa de ensamblador reducido línea por línea.

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
        Verifica que una instrucción sea válida y registra etiquetas si corresponde.
        """

        palabras: list[str] = SeparadorPalabras.separar_palabras(instruccion, None)
        if not palabras:
            return
        if self.__es_etiqueta(palabras, linea):
            self.__etiquetas.append(palabras[0][:-1])
            return
        codop: str = palabras[0]
        operandos: list[str] = palabras[1:]

        self.__validar_codop(codop, linea)
        self.__validar_cantidad_operandos(codop, operandos, linea)

    def __es_etiqueta(self, palabras_instruccion: list[str], linea: int) -> bool:
        """
        Determina si una instrucción corresponde a una etiqueta.

        :param palabras_instruccion: Componentes de la instrucción separada en palabras.
        :type palabras_instruccion: list
        :param linea: Línea donde se encuentra la instrucción.
        :type linea: int
        :return: True si es una etiqueta, False en caso contrario.
        """

        if len(palabras_instruccion) != 1:
            return False
        etiqueta: str = palabras_instruccion[0]
        if etiqueta[-1] != ":":
            return False
        nombre_etiqueta: str = etiqueta[:-1]
        self.__validar_etiqueta(nombre_etiqueta, linea)
        return True

    def __validar_etiqueta(self, nombre_etiqueta: str, linea: int):
        """
        Verifica que una etiqueta cumpla con las reglas de sintaxis.
        """

        if nombre_etiqueta is None or nombre_etiqueta == "":
            raise ValueError(f"La etiqueta en la línea {linea} debe tener nombre.")
        if not nombre_etiqueta.isalnum():
            raise ValueError(f"La etiqueta {nombre_etiqueta} de la línea {linea} debe ser alfanumérica.")
        if not nombre_etiqueta[0].isalpha():
            raise ValueError(f"La etiqueta {nombre_etiqueta} de la línea {linea} debe iniciar con una letra.")
        if nombre_etiqueta in self.__etiquetas:
            raise ValueError(f"La etiqueta {nombre_etiqueta} de la línea {linea} ya existe.")

    def __validar_codop(self, codop: str, linea: int):
        """
        Verifica que el código de operación exista.
        """

        if codop not in self.__nombres_codops:
            raise ValueError(f"Código de operación '{codop}' desconocido en la línea {linea}")

    def __validar_cantidad_operandos(self, codop: str, operandos: list[str], linea: int):
        """
        Verifica que la cantidad de operandos coincida con la requerida por el código de operación.

        :raises ValueError: Si la cantidad de operandos no es la esperada.
        """

        cantidad_operandos_esperados: int = self.__obtener_cantidad_operandos_codop(codop)

        if len(operandos) != cantidad_operandos_esperados:
            raise ValueError(
                f"La instrucción con código de operación '{codop}' en la línea {linea} espera "
                f"{cantidad_operandos_esperados} operandos, pero se proporcionaron {len(operandos)}."
            )

    def __obtener_cantidad_operandos_codop(self, codop: str) -> int:
        """
        Obtiene la cantidad de operandos esperados para un código de operación dado.
        """

        for codop_info in self.__info_codops:
            if codop_info["nombre"] == codop:
                return codop_info["cantidad_operandos"]

        raise ValueError(f"Código de operación '{codop}' desconocido")
