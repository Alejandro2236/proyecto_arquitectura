class UnidadControl:
    __CODOPS: dict = {
        "00000": {"nombre": "ADD", "cantidad_operandos": 3},
        "00001": {"nombre": "SUB", "cantidad_operandos": 3},
        "00010": {"nombre": "MUL", "cantidad_operandos": 3},
        "00011": {"nombre": "DIV", "cantidad_operandos": 3},
    }

    @property
    def codops(self):
        """Proporciona acceso de sólo lectura al mapa de codops."""
        return self.__CODOPS
