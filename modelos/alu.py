import struct

class Alu:
    def __init__(self):
        self.__operando1: str = ""
        self.__operando2: str = ""
        self.__codop: str = ""
        self.__resultado: str = ""
        self.__flags: dict = {
            "Z": 0,  # Zero
            "C": 0,  # Carry
            "N": 0,  # Negative
            "O": 0,  # Overflow
        }

    def ejecutar(self, codop: str, operando1: str, tipo1: str, operando2: str, tipo2: str):
        self.__codop = codop
        self.__operando1 = operando1
        self.__operando2 = operando2

        # Convertir operandos a un formato común para operar
        valor1 = self._convertir_operando(operando1, tipo1)
        valor2 = self._convertir_operando(operando2, tipo2)

        # Realizar operación
        resultado = self._operar(codop, valor1, valor2)

        # Actualizar resultado y flags
        self.__resultado = resultado
        self._actualizar_flags(resultado, tipo1)
        return self.__resultado

    def _convertir_operando(self, operando, tipo):
        """
        Convierte un operando al tipo correspondiente.
        """
        if tipo == "entero":
            return int(operando, 2)  # Asume binario
        elif tipo == "flotante":
            # Determinar si es decimal o binario IEEE 754
            if self._es_binario(operando):
                return self._binario_a_flotante(operando)  # Convertir binario IEEE 754
            else:
                return float(operando)  # Decimal
        else:
            raise ValueError(f"Tipo de operando no soportado: {tipo}")

    def _es_binario(self, operando):
        """
        Determina si un operando es binario (solo contiene 0s y 1s).
        """
        return all(c in "01" for c in operando)

    def _binario_a_flotante(self, binario):
        """
        Convierte un número binario IEEE 754 a flotante.
        :param binario: Cadena binaria de 32 bits (IEEE 754 precisión simple).
        :return: Número flotante equivalente.
        """
        if len(binario) != 32:
            raise ValueError("El formato IEEE 754 debe tener 32 bits (precisión simple).")
        entero = int(binario, 2)  # Convertir binario a entero
        bytes_binarios = entero.to_bytes(4, byteorder="big")  # 4 bytes (32 bits)
        return struct.unpack(">f", bytes_binarios)[0]  # Desempaquetar a flotante

    def _operar(self, codop, valor1, valor2):
        if codop == "ADD":
            return valor1 + valor2
        elif codop == "SUB":
            return valor1 - valor2
        elif codop == "MUL":
            return valor1 * valor2
        elif codop == "DIV":
            return valor1 / valor2 if valor2 != 0 else float("inf")
        else:
            raise ValueError(f"Código de operación no soportado: {codop}")

    def _actualizar_flags(self, resultado, tipo):
        if tipo == "entero":
            valor = int(resultado)
            self.__flags["Z"] = int(valor == 0)
            self.__flags["N"] = int(valor < 0)
        elif tipo == "flotante":
            valor = float(resultado)
            self.__flags["Z"] = int(valor == 0.0)
            self.__flags["N"] = int(valor < 0.0)

    def obtener_resultado(self):
        return self.__resultado

    def obtener_flags(self):
        return self.__flags
