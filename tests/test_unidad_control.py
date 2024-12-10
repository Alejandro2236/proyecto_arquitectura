import unittest

from modelos.bus_control import BusControl
from modelos.bus_datos import BusDatos
from modelos.bus_direcciones import BusDirecciones
from modelos.estado_ciclo_instruccion import EstadoCicloInstruccion
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

        unidad_control = UnidadControl()
        unidad_control_cableada = UnidadControlCableada(
            pc,
            mar,
            mbr,
            bus_datos,
            bus_direcciones,
            bus_control,
            memoria_instrucciones,
            ir,
            unidad_control
        )

        unidad_control.continuar_ciclo_instrucciones()

        self.assertEqual("00000011100000000100000000000000100000000000011", ir.registro)

    def test_decode_instruction_sin_co(self):
        ir = Ir()
        ir.registro = "00000011100000000100000000000000100000000000011"
        unidad_control = UnidadControl()
        unidad_control.asignar_estado_para_tests(EstadoCicloInstruccion.FI)
        unidad_control_cableada = UnidadControlCableada(ir, unidad_control)

        unidad_control.continuar_ciclo_instrucciones()

        self.assertEqual("00000011100000000100000000000000100000000000011", unidad_control.instruccion_actual)
        self.assertEqual("ADD", unidad_control.operacion_actual)
        self.assertEqual("0000000010", unidad_control.operando1)
        self.assertEqual("registro", unidad_control.direccionamiento_operando1)
        self.assertEqual("0000000001", unidad_control.operando2)
        self.assertEqual("int", unidad_control.tipo_operando2)
        self.assertEqual("0000000011", unidad_control.operando3)
        self.assertEqual("int", unidad_control.tipo_operando3)
        self.assertEqual(EstadoCicloInstruccion.EI, unidad_control.estado_siguiente_a_di)

    def test_decode_instruction_con_co(self):
        ir = Ir()
        ir.registro = "00010101100000000100111000000001010010000000000"
        unidad_control = UnidadControl()
        unidad_control.asignar_estado_para_tests(EstadoCicloInstruccion.FI)
        unidad_control_cableada = UnidadControlCableada(ir, unidad_control)

        unidad_control.continuar_ciclo_instrucciones()

        self.assertEqual("00010101100000000100111000000001010010000000000", unidad_control.instruccion_actual)
        self.assertEqual("MUL", unidad_control.operacion_actual)
        self.assertEqual("0000000010", unidad_control.operando1)
        self.assertEqual("directo_datos", unidad_control.direccionamiento_operando1)
        self.assertEqual("0000000010", unidad_control.operando2)
        self.assertEqual("desconocido", unidad_control.tipo_operando2)
        self.assertEqual("0000000000", unidad_control.operando3)
        self.assertEqual("float", unidad_control.tipo_operando3)
        self.assertEqual(EstadoCicloInstruccion.CO, unidad_control.estado_siguiente_a_di)

