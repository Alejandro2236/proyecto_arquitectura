from typing import Optional

from modelos.unidad_control import UnidadControl


class ControladorUnidadControl:
    def __init__(self):
        self.__unidad_control: Optional[UnidadControl] = None
        self.__dict_codops: Optional[dict] = None

    def crear_unidad_control(self):
        self.__unidad_control: UnidadControl = UnidadControl()

    def obtener_nombres_codop(self) -> set[str]:
        self.__validar_unidad_control()
        self.__inicializar_dict_codops()
        nombres_codops: set = {info["nombre"] for info in self.__dict_codops}
        return nombres_codops

    def obtener_info_codops(self) -> list[dict]:
        self.__validar_unidad_control()
        self.__inicializar_dict_codops()
        info_codops = list(self.__dict_codops.values())
        return info_codops

    def __validar_unidad_control(self):
        if self.__unidad_control is None:
            raise ValueError("La unidad de control no ha sido inicializada.")

    def __inicializar_dict_codops(self) -> None:
        if self.__dict_codops is None:
            self.__dict_codops: dict = self.__unidad_control.codops
