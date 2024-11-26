from modelos.memoria_base import MemoriaBase


class MemoriaDatos(MemoriaBase):

    def __init__(self, capacidad: int):
        super().__init__(capacidad)
