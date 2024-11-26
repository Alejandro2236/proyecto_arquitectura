from abc import ABC


class MemoriaBase(ABC):

    def __init__(self, capacidad: int):
        self._capacidad = capacidad
        self._direcciones: list = [0] * capacidad
        self._indicacion_control = None
        self._direccion_actual = None

    @property
    def indicacion_control(self):
        raise AttributeError("La señal de control no es accesible desde el exterior.")

    @indicacion_control.setter
    def indicacion_control(self, value: int):
        if value not in (0, 1):
            raise ValueError("La señal de control debe ser 0 (lectura) o 1 (escritura).")
        self._indicacion_control: int = value
