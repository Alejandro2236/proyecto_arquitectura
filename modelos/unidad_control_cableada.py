from typing import TYPE_CHECKING

from modelos.memoria_datos import MemoriaDatos

if TYPE_CHECKING:
    from modelos.mar import Mar
    from modelos.mbr import Mbr
    from modelos.memoria_instrucciones import MemoriaInstrucciones


class UnidadControlCableada:
    def __init__(self, *instancias):
        self.__componentes: dict = {instancia.__class__.__name__.lower(): instancia for instancia in instancias}
        for instancia in instancias:
            if instancia.__class__.__name__.lower() == "unidadcontrol":
                instancia.asignar_unidad_control_cableada(self)

    def mover_valor(
        self,
        nombre_clase_origen: str,
        nombre_clase_destino: str,
        atributo_origen: str,
        atributo_destino: str
    ):
        """
        Mueve el valor de un atributo origen de una clase origen a un atributo destino de una clase destino.

        :param nombre_clase_origen: Nombre de la clase que tiene el atributo origen en minuscula
        :param nombre_clase_destino: Nombre de la clase que tiene el atributo destino en minuscula
        :param atributo_origen: El atributo del que se sacará el valor
        :param atributo_destino: El atrubuto donde se escribirá el valor
        :return: None
        """

        clase_origen = self.__componentes[nombre_clase_origen]
        clase_destino = self.__componentes[nombre_clase_destino]

        if not clase_origen:
            raise ValueError(f"La clase de origen {nombre_clase_origen} no fue encontrada.")
        if not clase_destino:
            raise ValueError(f"La clase de destino {nombre_clase_destino} no fue encontrada")

        if not hasattr(clase_origen, atributo_origen):
            raise AttributeError(f"{nombre_clase_origen} no tiene atributo {atributo_origen}")
        if not hasattr(clase_destino, atributo_destino):
            raise AttributeError(f"{nombre_clase_destino} no tiene atributo {atributo_destino}")

        valor = getattr(clase_origen, atributo_origen)
        setattr(clase_destino, atributo_destino, valor)

    def enviar_dato(self, valor: str, nombre_clase_destino: str, atributo_destino: str):
        clase_destino = self.__componentes[nombre_clase_destino]
        if not clase_destino:
            raise ValueError(f"La clase de destino {nombre_clase_destino} no fue encontrada")
        if not hasattr(clase_destino, atributo_destino):
            raise AttributeError(f"{nombre_clase_destino} no tiene atributo {atributo_destino}")
        setattr(clase_destino, atributo_destino, valor)

    def enviar_direccion_a_mar(self, direccion: str):
        mar: Mar = self.__componentes["mar"]
        mar.registro = direccion

    def enviar_dato_a_mbr(self, dato: str):
        mbr: Mbr = self.__componentes["mbr"]
        mbr.registro = dato

    def activar_memoria_instrucciones(self):
        memoria_instrucciones: MemoriaInstrucciones = self.__componentes["memoriainstrucciones"]
        memoria_instrucciones.ejecutar_indicacion_control()

    def activar_memoria_datos(self):
        memoria_datos: MemoriaDatos = self.__componentes["memoriadatos"]
        memoria_datos.ejecutar_indicacion_control()
