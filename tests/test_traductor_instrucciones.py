import unittest

from controladores.controlador_unidad_control import ControladorUnidadControl
from ensambladores.traductor_instrucciones import TraductorInstrucciones


class TestCaseTraductorInstrucciones(unittest.TestCase):
    def test_traducir_programa_datos_int(self):
        controlador_unidad_control = ControladorUnidadControl()
        controlador_unidad_control.crear_unidad_control()
        traductor_instrucciones = TraductorInstrucciones(controlador_unidad_control)

        programa_traducido = traductor_instrucciones.traducir_programa(["ADD R2 1 3"])
        print(programa_traducido)
        self.assertIsNotNone(programa_traducido)
