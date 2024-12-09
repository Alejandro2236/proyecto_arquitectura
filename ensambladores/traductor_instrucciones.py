from controladores.controlador_memoria_datos import ControladorMemoriaDatos
from controladores.controlador_memoria_instrucciones import ControladorMemoriaInstrucciones
from controladores.controlador_unidad_control import ControladorUnidadControl
from utilidades import separador_palabras, transformador_binario, verificador_tipos


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

    def __init__(
        self,
        controlador_unidad_control: ControladorUnidadControl,
        controlador_memoria_datos: ControladorMemoriaDatos,
        controlador_memoria_instrucciones: ControladorMemoriaInstrucciones
    ):
        self.__mapa_codops_binarios = controlador_unidad_control.obtener_codigos_binarios_codops()
        self.__mapa_tipos_dato_binarios = controlador_unidad_control.obtener_codigos_binarios_tipos_dato()
        self.__formato_instrucciones = controlador_unidad_control.obtener_formato_instrucciones()
        self.__formato_floats = controlador_unidad_control.obtener_formato_float()
        self.__longitud_instrucciones = controlador_unidad_control.obtener_longitud_instrucciones()
        self.__mapa_tipos_direccionamiento_binarios = controlador_unidad_control.obtener_codigos_binarios_tipos_direccionamiento()
        self.__controlador_memoria_datos = controlador_memoria_datos
        self.__controlador_memoria_instrucciones = controlador_memoria_instrucciones
        self.__etiquetas_actuales: dict = {}

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

        posicion_inicial_memoria = self.__controlador_memoria_instrucciones.obtener_posicion_inicial_instrucciones(
            instrucciones
        )

        self.__etiquetas_actuales = {}
        programa_traducido = []
        contador_posicion_instruccion_local = 0

        for instruccion in instrucciones:
            if instruccion.strip() == "":
                continue
            if verificador_tipos.es_etiqueta(instruccion):
                nombre_etiqueta = instruccion[:-1]
                if nombre_etiqueta in self.__etiquetas_actuales:
                    raise ValueError("No se pueden tener dos etiquetas con el mismo nombre.")
                posicion_real_memoria = posicion_inicial_memoria + contador_posicion_instruccion_local
                posicion_real_memoria_binario = transformador_binario.transformar_int_en_complemento_a_dos(
                    str(posicion_real_memoria),
                    self.__formato_instrucciones["valor_operando1"]
                )
                self.__etiquetas_actuales[nombre_etiqueta] = posicion_real_memoria_binario
                continue
            instruccion_traducida: str = self.__traducir_instruccion(instruccion)
            programa_traducido.append(instruccion_traducida)
            contador_posicion_instruccion_local += 1
        print(self.__etiquetas_actuales)
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
            if indice == 0 and not verificador_tipos.es_registro(
                operando
            ) and not verificador_tipos.es_direccion_memoria(operando) and not verificador_tipos.es_etiqueta_operando(
                operando
            ):
                raise ValueError("El primer operando debe ser un registro, direccion de memoria o etiqueta")

            if verificador_tipos.es_int(operando):
                tipo_operando = self.__obtener_codigo_tipo("int")
                try:
                    valor_operando = transformador_binario.transformar_int_en_complemento_a_dos(
                        operando,
                        longitud_valor_operando
                    )
                    tipo_direccionamiento = self.__obtener_codigo_direccionamiento("inmediato")
                except ValueError:
                    valor_a_almacenar = transformador_binario.transformar_int_en_complemento_a_dos(
                        operando,
                        self.__longitud_instrucciones
                    )
                    valor_operando = self.__almacenar_y_obtener_posicion_binaria(
                        valor_a_almacenar,
                        longitud_valor_operando
                    )
                    tipo_direccionamiento = self.__obtener_codigo_direccionamiento("directo_datos")
            elif verificador_tipos.es_float(operando):
                tipo_operando = self.__obtener_codigo_tipo("float")
                valor_a_almacenar = transformador_binario.transformar_float_en_formato_binario(
                    operando,
                    self.__longitud_instrucciones,
                    self.__formato_floats["exponente"]
                )
                valor_operando = self.__almacenar_y_obtener_posicion_binaria(valor_a_almacenar, longitud_valor_operando)
                tipo_direccionamiento = self.__obtener_codigo_direccionamiento("directo_datos")
            elif verificador_tipos.es_registro(operando):
                tipo_operando = self.__obtener_codigo_tipo("desconocido")
                valor_operando = transformador_binario.transformar_int_en_complemento_a_dos(
                    operando[1:],
                    longitud_valor_operando
                )
                tipo_direccionamiento = self.__obtener_codigo_direccionamiento("registro")
            elif verificador_tipos.es_direccion_memoria(operando):
                tipo_operando = self.__obtener_codigo_tipo("desconocido")
                valor_operando = transformador_binario.transformar_int_en_complemento_a_dos(
                    operando[1:],
                    longitud_valor_operando
                )
                tipo_direccionamiento = self.__obtener_codigo_direccionamiento("directo_datos")
            elif verificador_tipos.es_etiqueta_operando(operando):
                tipo_operando = self.__obtener_codigo_tipo("desconocido")
                if operando not in self.__etiquetas_actuales:
                    raise ValueError("La etiqueta tiene que haberse declarado antes.")
                valor_operando = self.__etiquetas_actuales[operando]
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

    def __almacenar_y_obtener_posicion_binaria(self, valor_a_almacenar: str, longitud_operando) -> str:
        posicion = self.__calcular_posicion_para_almacenar_dato()
        self.__almacenar_en_posicion(valor_a_almacenar, posicion)
        return transformador_binario.transformar_int_en_complemento_a_dos(str(posicion), longitud_operando)

    def __calcular_posicion_para_almacenar_dato(self) -> int:
        return self.__controlador_memoria_datos.obtener_siguiente_posicion_libre()

    def __almacenar_en_posicion(self, valor_a_almacenar: str, posicion: int) -> None:
        self.__controlador_memoria_datos.almacenar_dato_en_posicion(valor_a_almacenar, posicion)

    @staticmethod
    def __generar_operando_vacio(
        longitud_direccionamiento: int,
        longitud_tipo_operando: int,
        longitud_valor_operando: int
    ) -> str:
        operador_vacio = "0" * longitud_direccionamiento + "0" * longitud_tipo_operando + "0" * longitud_valor_operando
        return operador_vacio
