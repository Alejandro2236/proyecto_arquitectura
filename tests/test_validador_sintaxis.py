import unittest

from ensambladores.validador_sintaxis import ValidadorSintaxis


class MyTestCase(unittest.TestCase):
    def test_validar_programa_correcto(self):
        validador = ValidadorSintaxis(
            {
                "00000": {"nombre": "ADD", "cantidad_operandos": 3},
                "00001": {"nombre": "SUB", "cantidad_operandos": 3},
                "00010": {"nombre": "MUL", "cantidad_operandos": 3},
                "00011": {"nombre": "DIV", "cantidad_operandos": 3},
            }
        )
        programa_correcto = ["ADD R1 R2 R3", "SUB R1 R3 R2", "MUL R2 R4 R1"]

        es_correcto = validador.validar_programa(programa_correcto)
        self.assertTrue(es_correcto)

    def test_validar_programa_operacion_inexistente(self):
        validador = ValidadorSintaxis(
            {
                "00000": {"nombre": "ADD", "cantidad_operandos": 3},
                "00001": {"nombre": "SUB", "cantidad_operandos": 3},
                "00010": {"nombre": "MUL", "cantidad_operandos": 3},
                "00011": {"nombre": "DIV", "cantidad_operandos": 3},
            }
        )
        programa_correcto = ["ADD R1 R2 R3", "SUB R1 R3 R2", "INEX R2 R4 R1"]

        with self.assertRaises(ValueError):
            validador.validar_programa(programa_correcto)
