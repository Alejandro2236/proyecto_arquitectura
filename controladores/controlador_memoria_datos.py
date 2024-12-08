from typing import Optional

from modelos.memoria_datos import MemoriaDatos


class ControladorMemoriaDatos():

    def __init__(self):
        self.__memoria_datos: Optional[MemoriaDatos] = None

    def crear_memoria_datos(self, capacidad: int):
        if self.__memoria_datos is not None:
            raise ValueError("La memoria de datos ya existe.")
        self.__memoria_datos: MemoriaDatos = MemoriaDatos(capacidad)

    def obtener_siguiente_posicion_libre(self) -> int:
        self.__validar_memoria_datos()
        siguiente_posicion_libre = self.__memoria_datos.siguiente_posicion_libre
        return siguiente_posicion_libre

    def almacenar_dato_en_posicion(self, dato: str, posicion: int):
        if dato == "":
            raise ValueError("El dato no puede estar vacío.")

        if 0 >= posicion >= self.__memoria_datos.capacidad:
            raise ValueError(f"La posición de memoria debe estar entre 0 y {self.__memoria_datos.capacidad}.")

        self.__memoria_datos.almacenar_dato_en_posicion(dato, posicion)

    def __validar_memoria_datos(self):
        if self.__memoria_datos is None:
            raise ValueError("La memoria de datos no ha sido inicializada.")
