from modelos.memoria_instrucciones import MemoriaInstrucciones


class ControladorMemoriaInstrucciones:
    def __init__(self):
        self.__memoria_instrucciones = None

    def crear_memoria_instrucciones(self, capacidad: int):
        self.__memoria_instrucciones = MemoriaInstrucciones(capacidad)

    def escribir_programa_en_memoria(self, programa_traducido: list[str]):
        raise NotImplementedError
