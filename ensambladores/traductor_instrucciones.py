from controladores.controlador_unidad_control import ControladorUnidadControl
from utilidades import separador_palabras, transformador_binario


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
        self.__formato_floats = controlador_unidad_control.obtener_formato_float()
        self.__longitud_instrucciones = controlador_unidad_control.obtener_longitud_instrucciones()
        self.__mapa_tipos_direccionamiento_binarios = controlador_unidad_control.obtener_codigos_binarios_tipos_direccionamiento()

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
        return programa_traducido

    def __traducir_instruccion(self, instruccion: str) -> str:
        if instruccion is None:
            raise ValueError("Debe pasar una instrucción para traducir.")
        palabras: list[str] = separador_palabras.separar_palabras(instruccion, None)
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
        lista_operandos_traducidos: list = []

        longitud_tipo_operando: int = self.__formato_instrucciones["tipo_operando1"]
        longitud_direccionamiento: int = self.__formato_instrucciones["direccionamiento_operando1"]
        longitud_valor_operando: int = self.__formato_instrucciones["valor_operando1"]

        for indice, operando in enumerate(operandos):
            if indice == 0 and not self.__es_registro(operando) and not self.__es_direccion_memoria(
                operando
            ) and not self.__es_etiqueta(operando):
                raise ValueError("El primer operando debe ser un registro, direccion de memoria o etiqueta")

            if self.__es_int(operando):
                tipo_operando = self.__obtener_codigo_tipo("int")
                try:
                    valor_operando = transformador_binario.transformar_int_en_complemento_a_dos(
                        operando,
                        longitud_valor_operando
                    )
                    tipo_direccionamiento = self.__obtener_codigo_direccionamiento("inmediato")
                except:
                    valor_operando = transformador_binario.transformar_int_en_complemento_a_dos(
                        operando,
                        self.__longitud_instrucciones
                    )
                    tipo_direccionamiento = self.__obtener_codigo_direccionamiento("directo_datos")
            elif self.__es_float(operando):
                tipo_operando = self.__obtener_codigo_tipo("float")
                valor_operando = transformador_binario.transformar_float_en_formato_binario(
                    operando,
                    self.__longitud_instrucciones,
                    self.__formato_floats["exponente"]
                )
                tipo_direccionamiento = self.__obtener_codigo_direccionamiento("directo_datos")
            else:
                raise ValueError(f"Formato no reconocido para el operando {operando}")

            operando_completo = tipo_direccionamiento + tipo_operando + valor_operando
            lista_operandos_traducidos.append(operando_completo)

        while len(lista_operandos_traducidos) < 3:
            lista_operandos_traducidos.append(
                self.__generar_operando_vacio(
                    longitud_direccionamiento,
                    longitud_tipo_operando,
                    longitud_valor_operando
                )
            )

        return lista_operandos_traducidos

    def __es_int(self, operando: str) -> bool:
        if not operando.isdigit():
            if not (operando.startswith("-") and operando[1:].isdigit()):
                return False
        return True

    def __es_float(self, operando: str) -> bool:
        try:
            float(operando)
            if "." not in operando:
                return False
            return True
        except ValueError:
            return False

    def __es_registro(self, operando: str) -> bool:
        print(operando)
        if not operando.startswith('R'):
            return False
        if not operando[1:].isdigit():
            return False
        return True

    def __es_direccion_memoria(self, operando: str) -> bool:
        if not operando.startswith("#"):
            return False
        if not operando[1:].isdigit():
            return False
        return True

    def __es_etiqueta(self, operando: str) -> bool:
        pass

    def __obtener_codigo_tipo(self, tipo: str) -> str:
        for key, value in self.__mapa_tipos_dato_binarios.items():
            if value == tipo:
                return key
        raise ValueError(f"Tipo de operando no soportado: {tipo}")

    def __obtener_codigo_direccionamiento(self, direccionamiento: str) -> str:
        for key, value in self.__mapa_tipos_direccionamiento_binarios.items():
            if value == direccionamiento:
                return key
        raise ValueError(f"Modo de direccionamiento no soportado: {direccionamiento}")

    def __generar_operando_vacio(
        self,
        longitud_direccionamiento: int,
        longitud_tipo_operando: int,
        longitud_valor_operando: int
    ) -> str:
        operador_vacio = "0" * longitud_direccionamiento + "0" * longitud_tipo_operando + "0" * longitud_valor_operando
        return operador_vacio
