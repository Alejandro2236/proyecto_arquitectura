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

    @property
    def codops(self):
        """Proporciona acceso de sólo lectura al mapa de codops."""
        return self.__CODOPS
