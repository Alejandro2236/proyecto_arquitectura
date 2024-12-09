import unittest

from modelos.bus_control import BusControl
from modelos.bus_datos import BusDatos
from modelos.bus_direcciones import BusDirecciones
from modelos.ir import Ir
from modelos.mar import Mar
from modelos.mbr import Mbr
from modelos.memoria_instrucciones import MemoriaInstrucciones
from modelos.pc import Pc
from modelos.unidad_control import UnidadControl
from modelos.unidad_control_cableada import UnidadControlCableada


class TestCaseUnidadControl(unittest.TestCase):
    def test_fetch_instruction(self):
        pc = Pc()
        mar = Mar()
        mbr = Mbr()
        bus_direcciones = BusDirecciones()
        bus_datos = BusDatos()
        bus_control = BusControl()
        memoria_instrucciones = MemoriaInstrucciones(128)

        mar.bus_direcciones = bus_direcciones
        mbr.bus_datos = bus_datos
        bus_datos.mbr = mbr
        memoria_instrucciones.bus_control = bus_control
        memoria_instrucciones.bus_direcciones = bus_direcciones
        memoria_instrucciones.bus_datos = bus_datos
        memoria_instrucciones.almacenar_dato_en_posicion("00000011100000000100000000000000100000000000011", 0)
        ir = Ir()

        unidad_control_cableada = UnidadControlCableada(
            pc,
            mar,
            mbr,
            bus_datos,
            bus_direcciones,
            bus_control,
            memoria_instrucciones,
            ir
        )
        unidad_control = UnidadControl(unidad_control_cableada)

        unidad_control.continuar_ciclo_instrucciones()

        self.assertEqual(ir.registro, "00000011100000000100000000000000100000000000011")
