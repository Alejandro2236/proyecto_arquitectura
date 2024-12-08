from modelos.mar import Mar
from modelos.mbr import Mbr


class UnidadControlCableada:
    def __init__(self, diccionario_componentes: dict):
        self.__componentes: dict = diccionario_componentes

    def mover_valor(self, origen: str, destino: str):
        ...

    def enviar_direccion_a_mar(self, direccion: str):
        mar: Mar = self.__componentes["mar"]
        mar.registro = direccion

    def enviar_dato_a_mbr(self, dato: str):
        mbr: Mbr = self.__componentes["mbr"]
        mbr.registro = dato
