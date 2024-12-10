from typing import Optional

from modelos.memoria_instrucciones import MemoriaInstrucciones
from utilidades import verificador_tipos


class ControladorMemoriaInstrucciones:
    def __init__(self):
        self.__memoria_instrucciones: Optional[MemoriaInstrucciones] = None

    def crear_memoria_instrucciones(self, capacidad: int):
        if self.__memoria_instrucciones is not None:
            raise ValueError("La memoria de instrucciones ya ha sido creada.")
        self.__memoria_instrucciones: MemoriaInstrucciones = MemoriaInstrucciones(capacidad)

    def obtener_memoria_instrucciones(self) -> MemoriaInstrucciones:
        return self.__memoria_instrucciones

    def obtener_siguiente_posicion_libre(self) -> int:
        self.__validar_memoria_instrucciones()
        siguiente_posicion_libre = self.__memoria_instrucciones.siguiente_posicion_libre
        return siguiente_posicion_libre

    def obtener_posicion_inicial_instrucciones(self, instrucciones: list[str]) -> int:
        longitud_programa = 0
        for instruccion in instrucciones:
            if verificador_tipos.es_etiqueta(instruccion) or instruccion.strip() == "":
                continue
            longitud_programa += 1
        posiciones_libres = self.__memoria_instrucciones.posiciones_libres
        for posicion_libre in posiciones_libres:
            if posicion_libre + longitud_programa > self.__memoria_instrucciones.capacidad:
                raise ValueError("El programa no cabe en las posiciones libres.")
            continuar_externo: bool = False
            for indice in range(longitud_programa):
                if self.__memoria_instrucciones._direcciones[posicion_libre + indice] != 0:
                    continuar_externo = True
            if continuar_externo:
                continue
            return posicion_libre
        raise ValueError("Memoria demasiado llena para recibir instrucciones.")

    def escribir_programa_en_memoria(self, programa_traducido: list[str], posicion_inicial: int):
        for indice, instruccion in programa_traducido:
            self.__memoria_instrucciones.almacenar_dato_en_posicion(instruccion, posicion_inicial + indice)

    def __validar_memoria_instrucciones(self):
        if self.__memoria_instrucciones is None:
            raise ValueError("La memoria de datos no ha sido inicializada.")
