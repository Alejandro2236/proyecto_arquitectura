from abc import ABC


class MemoriaBase(ABC):

    def __init__(self, capacidad: int):
        self._capacidad = capacidad
        self._direcciones: list = [0] * self._capacidad
        self._indicacion_control = None
        self._direccion_actual = None

    @property
    def capacidad(self):
        """Proporciona acceso de sólo lectura a la capacidad"""
        return self._capacidad

    @property
    def indicacion_control(self):
        raise AttributeError("La señal de control no es accesible desde el exterior.")

    @indicacion_control.setter
    def indicacion_control(self, indicacion_control: int):
        if indicacion_control not in (0, 1):
            raise ValueError("La señal de control debe ser 0 (lectura) o 1 (escritura).")
        self._indicacion_control: int = indicacion_control

    @property
    def direccion_actual(self):
        raise AttributeError("La dirección actual no es accesible desde el exterior.")

    @direccion_actual.setter
    def direccion_actual(self, direccion_actual: int):
        if direccion_actual not in range(self._capacidad):
            raise ValueError(f"La dirección actual debe estar entre 0 y {self._capacidad - 1}")
        self._direccion_actual: int = direccion_actual

    @property
    def siguiente_posicion_libre(self):
        """Proporciona acceso de sólo lectura a la siguiente posición libre"""
        for posicion, direccion in enumerate(self._direcciones):
            if direccion == 0:
                return posicion

    @property
    def posiciones_libres(self):
        """Proporciona acceso de sólo lectura a las posiciones libres"""
        posiciones_libres = []
        for posicion, direccion in enumerate(self._direcciones):
            if direccion == 0:
                posiciones_libres.append(posicion)
        return posiciones_libres

    def almacenar_dato_en_posicion(self, dato: str, posicion: int):
        self._direcciones[posicion] = dato
