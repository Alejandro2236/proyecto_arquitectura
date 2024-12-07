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
