import unittest

from controladores.controlador_memoria_datos import ControladorMemoriaDatos
from controladores.controlador_unidad_control import ControladorUnidadControl
from ensambladores.traductor_instrucciones import TraductorInstrucciones


class TestCaseTraductorInstrucciones(unittest.TestCase):
    def test_traducir_programa_datos_int(self):
        controlador_unidad_control = ControladorUnidadControl()
        controlador_unidad_control.crear_unidad_control()
        controlador_memoria_datos = ControladorMemoriaDatos()
        controlador_memoria_datos.crear_memoria_datos(32)
        traductor_instrucciones = TraductorInstrucciones(controlador_unidad_control, controlador_memoria_datos)

        programa_traducido = traductor_instrucciones.traducir_programa(["ADD R2 1 3", "MUL #2 R2 5.0", "HLT"])
        print(programa_traducido)
        self.assertIsNotNone(programa_traducido)
