from typing import Optional

from modelos.unidad_control import UnidadControl


class ControladorUnidadControl:
    def __init__(self):
        self.__unidad_control: Optional[UnidadControl] = None
        self.__dict_codops: Optional[dict] = None

    def crear_unidad_control(self):
        self.__unidad_control: UnidadControl = UnidadControl()

    def obtener_nombres_codop(self) -> set[str]:
        if self.__unidad_control is None:
            raise ValueError("La unidad de control no ha sido inicializada.")

        self.__inicializar_dict_codops()
        nombres_codops: set = {info["nombre"] for info in self.__dict_codops}
        return nombres_codops

    def __inicializar_dict_codops(self):
        if self.__dict_codops is None:
            self.__dict_codops: dict = self.__unidad_control.codops
