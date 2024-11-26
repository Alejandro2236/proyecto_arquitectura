import unittest

from controladores.controlador_unidad_control import ControladorUnidadControl
from ensambladores.validador_sintaxis import ValidadorSintaxis


class MyTestCase(unittest.TestCase):
    def test_validar_programa_correcto(self):
        controlador_unidad_control = ControladorUnidadControl()
        controlador_unidad_control.crear_unidad_control()
        validador = ValidadorSintaxis(controlador_unidad_control)
        programa_correcto = ["ADD R1 R2 R3", "SUB R1 R3 R2", "MUL R2 R4 R1"]

        es_correcto = validador.validar_programa(programa_correcto)
        self.assertTrue(es_correcto)

    def test_validar_programa_operacion_inexistente(self):
        controlador_unidad_control = ControladorUnidadControl()
        controlador_unidad_control.crear_unidad_control()
        validador = ValidadorSintaxis(controlador_unidad_control)
        programa_correcto = ["ADD R1 R2 R3", "SUB R1 R3 R2", "INEX R2 R4 R1"]

        with self.assertRaises(ValueError):
            validador.validar_programa(programa_correcto)
