from typing import Optional

from modelos.unidad_control import UnidadControl


class ControladorUnidadControl:
    def __init__(self):
        self.__unidad_control: Optional[UnidadControl] = None
        self.__dict_codops: Optional[dict] = None
        self.__info_codops: Optional[list] = None
        self.__tipos_dato: Optional[dict] = None
        self.__formato_instrucciones: Optional[dict] = None

    def crear_unidad_control(self):
        self.__unidad_control: UnidadControl = UnidadControl()

    def obtener_nombres_codop(self) -> set[str]:
        self.__inicializar_info_codops()
        nombres_codops: set = set({info["nombre"] for info in self.__info_codops})
        return nombres_codops

    def obtener_cantidad_operandos_codops(self) -> list[dict]:
        self.__inicializar_info_codops()
        lista_operandos = [{"nombre": info_codop["nombre"], "cantidad_operandos": info_codop["cantidad_operandos"]} for
                           info_codop in self.__info_codops]
        return lista_operandos

    def __validar_unidad_control(self):
        if self.__unidad_control is None:
            raise ValueError("La unidad de control no ha sido inicializada.")

    def __inicializar_dict_codops(self) -> None:
        if self.__dict_codops is None:
            self.__validar_unidad_control()
            self.__dict_codops: dict = self.__unidad_control.codops

    def __inicializar_info_codops(self) -> None:
        if self.__info_codops is None:
            self.__validar_unidad_control()
            self.__inicializar_dict_codops()
            self.__info_codops: list = list(self.__dict_codops.values())

    def obtener_codigos_binarios_codops(self) -> list[dict]:
        self.__inicializar_dict_codops()
        binarios_codop = [{"nombre": info_codops["nombre"], "codigo_binario": codigo_binario} for
                          codigo_binario, info_codops in self.__dict_codops.items()]
        return binarios_codop

    def obtener_codigos_binarios_tipos_dato(self) -> dict:
        self.__inicializar_tipos_dato()
        return self.__tipos_dato

    def __inicializar_tipos_dato(self) -> None:
        if self.__tipos_dato is None:
            self.__validar_unidad_control()
            self.__tipos_dato: dict = self.__unidad_control.tipos_dato

    def obtener_formato_instrucciones(self) -> dict:
        self.__inicializar_formato_instrucciones()
        return self.__formato_instrucciones

    def __inicializar_formato_instrucciones(self) -> None:
        if self.__formato_instrucciones is None:
            self.__validar_unidad_control()
            self.__formato_instrucciones: dict = self.__unidad_control.formato_instrucciones

    def obtener_longitud_instrucciones(self) -> int:
        self.__inicializar_formato_instrucciones()
        longitud_instrucciones: int = sum(self.__formato_instrucciones.values())
        return longitud_instrucciones
