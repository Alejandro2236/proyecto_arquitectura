import unittest

from modelos.ir import Ir
from modelos.mbr import Mbr
from modelos.unidad_control_cableada import UnidadControlCableada


class TestCaseUnidadControlCableada(unittest.TestCase):
    def test_mover_de_clase_a_otra(self):
        mbr = Mbr()
        mbr.registro = "valor_a_mover"
        ir = Ir()
        ir.registro = "valor_no_cambiado"
        unidad_control_cableada = UnidadControlCableada(mbr, ir)

        unidad_control_cableada.mover_valor("mbr", "ir", "registro", "registro")

        self.assertEqual(ir.registro, "valor_a_mover")
        self.assertEqual(mbr.registro, "valor_a_mover")
