class UnidadControl:
    __CODOPS: dict = {
        "00000": "ADD",
        "00001": "SUB",
        "00010": "MUL",
        "00011": "DIV",
    }

    @property
    def codops(self):
        """Proporciona acceso de sólo lectura al mapa de codops."""
        return self.__CODOPS
