from typing import Optional


class Registro:
    def __init__(self):
        self.__valor_registro: Optional[str] = None
        self.__tipo_registro: Optional[str] = None

    @property
    def valor_registro(self):
        return self.__valor_registro

    @valor_registro.setter
    def valor_registro(self, value):
        self.__valor_registro = value

    @property
    def tipo_registro(self):
        return self.__tipo_registro

    @tipo_registro.setter
    def tipo_registro(self, value):
        self.__tipo_registro = value
