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
        self.__mapa_codops_binarios = controlador_unidad_control.obtener_codigos_binarios_codops()
        self.__mapa_tipos_dato_binarios = controlador_unidad_control.obtener_codigos_binarios_tipos_dato()
        self.__formato_instrucciones = controlador_unidad_control.obtener_formato_instrucciones()
        self.__longitud_instrucciones = controlador_unidad_control.obtener_longitud_instrucciones()

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
        if not codop:
            raise ValueError("No puede haber codops faltantes.")
        for info_codop_binario in self.__mapa_codops_binarios:
            if info_codop_binario["nombre"] == codop:
                return info_codop_binario["codigo_binario"]
        raise ValueError(f"Codop {codop} no encontrado en la lista de codops.")

    def __traducir_operandos(self, operandos: list[str]) -> list[str]:
        cantidad_operandos = len(operandos)
        lista_operandos_traducidos: list = []

        longitud_tipo_operando: int = self.__formato_instrucciones["tipo_operando1"]
        longitud_direccionamiento: int = self.__formato_instrucciones["direccionamiento_operando1"]
        longitud_valor_operando: int = self.__formato_instrucciones["valor_operando1"]

        match cantidad_operandos:
            case 0:
                tipo_operando: str = "0" * longitud_tipo_operando
                tipo_direccionamiento: str = "0" * longitud_direccionamiento
                valor_operando: str = "0" * longitud_valor_operando
                operando_completo: str = tipo_operando + tipo_direccionamiento + valor_operando
                for _ in range(3):
                    lista_operandos_traducidos.append(operando_completo)
                return lista_operandos_traducidos
            case 1:
                operando1: str = operandos[0]
                # TODO crear la lógica para 1 operando y crear los otros 2 en 0
            # TODO crear la lógica del resto de casos
