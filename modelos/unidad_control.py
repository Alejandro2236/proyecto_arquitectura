from typing import Optional

from modelos.estado_ciclo_instruccion import EstadoCicloInstruccion
from modelos.unidad_control_cableada import UnidadControlCableada


class UnidadControl:
    __CODOPS: dict = {
        "00000": {"nombre": "ADD", "cantidad_operandos": 3},
        "00001": {"nombre": "SUB", "cantidad_operandos": 3},
        "00010": {"nombre": "MUL", "cantidad_operandos": 3},
        "00011": {"nombre": "DIV", "cantidad_operandos": 3},
        "00100": {"nombre": "AND", "cantidad_operandos": 3},
        "00101": {"nombre": "OR", "cantidad_operandos": 3},
        "00110": {"nombre": "XOR", "cantidad_operandos": 3},
        "00111": {"nombre": "NOT", "cantidad_operandos": 2},
        "01000": {"nombre": "LOAD", "cantidad_operandos": 2},
        "01001": {"nombre": "STORE", "cantidad_operandos": 2},
        "01010": {"nombre": "MOVE", "cantidad_operandos": 2},
        "01011": {"nombre": "JMP", "cantidad_operandos": 1},
        "01100": {"nombre": "JEQ", "cantidad_operandos": 1},
        "01101": {"nombre": "JNE", "cantidad_operandos": 1},
        "01110": {"nombre": "JLT", "cantidad_operandos": 1},
        "01111": {"nombre": "JGT", "cantidad_operandos": 1},
        "10000": {"nombre": "HLT", "cantidad_operandos": 0},
        "10001": {"nombre": "CMP", "cantidad_operandos": 2}
    }

    __FORMATO_INSTRUCCIONES: dict = {
        "codop": 5,
        "direccionamiento_operando1": 2,
        "tipo_operando1": 2,
        "valor_operando1": 10,
        "direccionamiento_operando2": 2,
        "tipo_operando2": 2,
        "valor_operando2": 10,
        "direccionamiento_operando3": 2,
        "tipo_operando3": 2,
        "valor_operando3": 10,
        "reservado": 1
    }

    __FORMATO_FLOATS: dict = {"signo": 1, "exponente": 11, "mantisa": 36}

    __TIPOS_DATO: dict = {"00": "int", "01": "float", "10": "bool", "11": "desconocido"}

    __TIPOS_DIRECCIONAMIENTO: dict = {
        "00": "inmediato",
        "01": "registro",
        "10": "directo_datos",
        "11": "directo_instrucciones"
    }

    def __init__(self):
        self.__unidad_control_cableada: Optional[UnidadControlCableada] = None
        self.__estado_actual: Optional[EstadoCicloInstruccion] = None
        self.__instruccion_actual: str = ""
        self.__operacion_actual: str = ""
        self.__operando1: str = ""
        self.__direccionamiento_operando1: str = ""
        self.__operando2: str = ""
        self.__direccion_operando2: str = ""
        self.__tipo_operando2: str = ""
        self.__tipo_direccionamineto_operando2: str = ""
        self.__operando3: str = ""
        self.__direccion_operando3: str = ""
        self.__tipo_operando3: str = ""
        self.__tipo_direccionamineto_operando3: str = ""
        self.__estado_siguiente_a_di: Optional[EstadoCicloInstruccion] = None
        self.__estado_siguiente_a_fo: Optional[EstadoCicloInstruccion] = None

    @property
    def codops(self):
        """Proporciona acceso de sólo lectura al mapa de codops."""
        return self.__CODOPS

    @property
    def formato_instrucciones(self):
        """Proporciona acceso de sólo lectura al mapa de formato de instrucciones"""
        return self.__FORMATO_INSTRUCCIONES

    @property
    def formato_floats(self):
        """Proporciona acceso de sólo lectura al mapa de formato de floats"""
        return self.__FORMATO_FLOATS

    @property
    def tipos_dato(self):
        """Proporciona acceso de sólo lectura al mapa de tipos de dato"""
        return self.__TIPOS_DATO

    @property
    def tipos_direccionamiento(self):
        """Proporciona acceso de sólo lectura al mapa de tipos de direccionamiento"""
        return self.__TIPOS_DIRECCIONAMIENTO

    @property
    def estado_actual(self):
        raise AttributeError("Elemento no accesible.")

    @property
    def instruccion_actual(self):
        return self.__instruccion_actual

    @instruccion_actual.setter
    def instruccion_actual(self, value):
        self.__instruccion_actual = value

    @property
    def unidad_control_cableada(self):
        return self.__unidad_control_cableada

    @property
    def operacion_actual(self):
        return self.__operacion_actual

    @property
    def operando1(self):
        return self.__operando1

    @property
    def direccionamiento_operando1(self):
        return self.__direccionamiento_operando1

    @property
    def operando2(self):
        return self.__operando2

    @operando2.setter
    def operando2(self, value):
        self.__operando2 = value

    @property
    def tipo_operando2(self):
        return self.__tipo_operando2

    @property
    def operando3(self):
        return self.__operando3

    @operando3.setter
    def operando3(self, value):
        self.__operando3 = value

    @property
    def tipo_operando3(self):
        return self.__tipo_operando3

    @property
    def estado_siguiente_a_di(self):
        return self.__estado_siguiente_a_di

    @estado_actual.setter
    def estado_actual(self, nuevo_estado):
        match nuevo_estado:
            case EstadoCicloInstruccion.FI:
                self.__estado_actual = nuevo_estado
                self.__fetch_instruction()
            case EstadoCicloInstruccion.DI:
                self.__estado_actual = nuevo_estado
                self.__decode_instruction()
            case EstadoCicloInstruccion.CO:
                self.__estado_actual = nuevo_estado
                self.__calculate_operand()
            case EstadoCicloInstruccion.FO:
                self.__estado_actual = nuevo_estado
                self.__fetch_operand()

    def asignar_unidad_control_cableada(self, unidad_control_cableada):
        self.__unidad_control_cableada = unidad_control_cableada

    def continuar_ciclo_instrucciones(self):
        if self.__estado_actual is None:
            self.estado_actual = EstadoCicloInstruccion.FI
            return
        if self.__estado_actual == EstadoCicloInstruccion.FI:
            self.estado_actual = EstadoCicloInstruccion.DI
            return
        if self.__estado_actual == EstadoCicloInstruccion.DI:
            self.estado_actual = self.__estado_siguiente_a_di
            return
        if self.__estado_actual == EstadoCicloInstruccion.CO:
            self.estado_actual = EstadoCicloInstruccion.FO

    def __fetch_instruction(self):
        if self.__unidad_control_cableada is None:
            raise ValueError("Unidad de control cableada no inicializada.")

        self.__unidad_control_cableada.mover_valor("pc", "mar", "registro", "registro")
        self.__unidad_control_cableada.enviar_dato("00", "buscontrol", "registro")
        self.__unidad_control_cableada.activar_memoria_instrucciones()
        self.__unidad_control_cableada.mover_valor("mbr", "ir", "registro", "registro")

    def __decode_instruction(self):
        self.__unidad_control_cableada.mover_valor("ir", "unidadcontrol", "registro", "instruccion_actual")
        codop_binario = self.__instruccion_actual[:self.__FORMATO_INSTRUCCIONES["codop"]]
        datos_codop = self.__obtener_datos_codop(codop_binario)
        self.__operacion_actual = datos_codop["nombre"]
        cantidad_operandos = datos_codop["cantidad_operandos"]
        if cantidad_operandos == 0:
            self.__estado_siguiente_a_di = EstadoCicloInstruccion.EI
            return
        if cantidad_operandos >= 1:
            codigo_direccionamiento_operando1 = self.__codigo_direccionamiento_operando1()
            self.__decodificar_operando1(codigo_direccionamiento_operando1)
        if cantidad_operandos >= 2:
            codigo_direccionamiento_operando2 = self.__codigo_direccionamiento_operando2()
            codigo_tipo_operando2 = self.__codigo_tipo_operando2()
            self.__decodificar_operando2(codigo_direccionamiento_operando2, codigo_tipo_operando2)
        if cantidad_operandos == 3:
            codigo_direccionamiento_operando3 = self.__codigo_direccionamiento_operando3()
            codigo_tipo_operando3 = self.__codigo_tipo_operando3()
            self.__decodificar_operando3(codigo_direccionamiento_operando3, codigo_tipo_operando3)

    def __obtener_datos_codop(self, codigo: str) -> dict:
        return self.__CODOPS[codigo]

    def __obtener_tipo_direccionamiento(self, codigo: str) -> str:
        return self.__TIPOS_DIRECCIONAMIENTO[codigo]

    def __obtener_tipo(self, codigo: str) -> str:
        return self.__TIPOS_DATO[codigo]

    def __codigo_direccionamiento_operando1(self) -> str:
        codigo_direccionamiento = self.__instruccion_actual[5:7]
        return codigo_direccionamiento

    def __codigo_direccionamiento_operando2(self) -> str:
        codigo_direccionamiento = self.__instruccion_actual[19:21]
        return codigo_direccionamiento

    def __codigo_direccionamiento_operando3(self) -> str:
        codigo_direccionamiento = self.__instruccion_actual[33:35]
        return codigo_direccionamiento

    def __codigo_tipo_operando2(self) -> str:
        codigo_tipo = self.__instruccion_actual[21:23]
        return codigo_tipo

    def __codigo_tipo_operando3(self) -> str:
        codigo_tipo = self.__instruccion_actual[35:37]
        return codigo_tipo

    def __decodificar_operando1(self, codigo_direccionamiento: str):
        self.__direccionamiento_operando1 = self.__obtener_tipo_direccionamiento(codigo_direccionamiento)
        self.__operando1 = self.__instruccion_actual[9:19]

    def __decodificar_operando2(self, codigo_direccionamiento: str, codigo_tipo: str):
        self.__tipo_operando2 = self.__obtener_tipo(codigo_tipo)
        self.__decodificar_operando_diferente_a_1(codigo_direccionamiento, 2)

    def __decodificar_operando3(self, codigo_direccionamiento: str, codigo_tipo: str):
        self.__tipo_operando3 = self.__obtener_tipo(codigo_tipo)
        self.__decodificar_operando_diferente_a_1(codigo_direccionamiento, 3)

    def __decodificar_operando_diferente_a_1(self, codigo_direccionamiento: str, numero_operando: int):
        direccionamiento_operando = self.__obtener_tipo_direccionamiento(codigo_direccionamiento)
        if self.__necesita_calcular_direccion(direccionamiento_operando):
            if numero_operando == 2:
                self.__tipo_direccionamineto_operando2 = direccionamiento_operando
            elif numero_operando == 3:
                self.__tipo_direccionamineto_operando3 = direccionamiento_operando
            if self.__estado_actual == EstadoCicloInstruccion.CO:
                return
            self.__estado_siguiente_a_di = EstadoCicloInstruccion.CO
            return
        if numero_operando == 2:
            self.__operando2 = self.__instruccion_actual[23:33]
        elif numero_operando == 3:
            self.__operando3 = self.__instruccion_actual[37:47]
        self.__estado_siguiente_a_di = EstadoCicloInstruccion.EI

    @staticmethod
    def __necesita_calcular_direccion(direccionamiento: str) -> bool:
        return direccionamiento == "directo_datos" or direccionamiento == "registro"

    def __calculate_operand(self):
        if self.__operando2 == "":
            self.__direccion_operando2 = self.__instruccion_actual[23:33]
            return
        if self.__operando3 == "":
            self.__direccion_operando3 = self.__instruccion_actual[37:47]

    def __fetch_operand(self):
        if self.__operando2 == "":
            self.__unidad_control_cableada.enviar_dato(self.__direccion_operando2, "mar", "registro")
            self.__unidad_control_cableada.enviar_dato("00", "buscontrol", "registro")
            self.__unidad_control_cableada.activar_memoria_datos()
            self.__unidad_control_cableada.mover_valor("mbr", "unidadcontrol", "registro", "operando2")
            if self.__operando3 == "":
                self.__estado_siguiente_a_fo = EstadoCicloInstruccion.CO
        if self.__operando3 == "":
            self.__unidad_control_cableada.enviar_dato(self.__direccion_operando3, "mar", "registro")
            self.__unidad_control_cableada.enviar_dato("00", "buscontrol", "registro")
            self.__unidad_control_cableada.activar_memoria_datos()
            self.__unidad_control_cableada.mover_valor("mbr", "unidadcontrol", "registro", "operando3")

    def asignar_estado_para_tests(self, estado: EstadoCicloInstruccion):
        self.__estado_actual = estado
