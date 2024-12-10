import unittest

from controladores.controlador_memoria_datos import ControladorMemoriaDatos
from controladores.controlador_memoria_instrucciones import ControladorMemoriaInstrucciones
from controladores.controlador_unidad_control import ControladorUnidadControl
from ensambladores.traductor_instrucciones import TraductorInstrucciones


class TestCaseTraductorInstrucciones(unittest.TestCase):
    def test_traducir_programa_datos_validos(self):
        controlador_unidad_control = ControladorUnidadControl()
        controlador_unidad_control.crear_unidad_control()
        controlador_memoria_datos = ControladorMemoriaDatos()
        controlador_memoria_datos.crear_memoria_datos(32)
        controlador_memoria_instrucciones = ControladorMemoriaInstrucciones()
        controlador_memoria_instrucciones.crear_memoria_instrucciones(32)
        traductor_instrucciones = TraductorInstrucciones(
            controlador_unidad_control,
            controlador_memoria_datos,
            controlador_memoria_instrucciones
        )

        programa_traducido = traductor_instrucciones.traducir_programa(
            ["inicio:", "ADD R2 1 3", "JMP inicio", "MUL #2 R2 5.0", "final:", "HLT"]
        )
        print("programa traducido:\n", programa_traducido)
        self.assertIsNotNone(programa_traducido)
