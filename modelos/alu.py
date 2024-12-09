from typing import Union
import math

class ALU:
    def __init__(self):
        self.__operando1: str = ""
        self.__operando2: str = ""
        self.__codop: str = ""
        self.__resultado: str = ""  # Resultado almacenado en binario
        self.__flags: dict = {"CARRY": 0, "ZERO": 0, "SIGN": 0, "OVERFLOW": 0}

    def __interpretar_tipo_dato(self, tipo_dato: str) -> str:
        """Interpreta el tipo de dato basado en su codificación binaria."""
        if tipo_dato == "00":
            return "int"
        elif tipo_dato == "01":
            return "float"
        elif tipo_dato == "10":
            return "bool"
        elif tipo_dato == "11":
            return "desconocido"
        else:
            raise ValueError(f"Tipo de dato no válido: {tipo_dato}")

    def __convertir_operando(self, operando: str, tipo_dato: str, bits: int = 48) -> Union[int, float, bool]:
        tipo = self.__interpretar_tipo_dato(tipo_dato)
        if tipo == "int":
            valor = int(operando, 2)
            if operando[0] == "1":  # Negativo en complemento a 2
                valor -= (1 << bits)
            return valor
        elif tipo == "float":
            return self.__binario_a_flotante(operando, bits)
        elif tipo == "bool":
            return bool(int(operando, 2))
        elif tipo == "desconocido":
            return operando  # Devuelve el operando tal cual
        else:
            raise ValueError(f"Tipo de dato no soportado: {tipo}")

    def __ajustar_a_48_bits(self, valor: int) -> str:
        """Convierte un entero a su representación binaria en 48 bits."""
        if valor < 0:  # Ajuste para números negativos
            valor = (1 << 48) + valor
        return f"{valor:048b}"

    def __guardar_resultado(self, resultado: Union[int, float, bool], tipo_dato: str, bits: int = 48) -> None:
        tipo = self.__interpretar_tipo_dato(tipo_dato)
        if tipo == "int":
            self.__resultado = self.__ajustar_a_48_bits(resultado)
        elif tipo == "float":
            self.__resultado = self.__flotante_a_binario(resultado, bits)
        elif tipo == "bool":
            self.__resultado = f"{int(resultado):01b}"  # Representación de un bit para bool
        else:
            raise ValueError(f"Tipo de dato no soportado para guardar resultado: {tipo}")

    def ejecutar(self, codop: str, operando1: str, operando2: str, tipo_dato1: str, tipo_dato2: str, bits: int = 48) -> str:
        self.__operando1 = operando1
        self.__operando2 = operando2
        self.__codop = codop

        operando1_valor = self.__convertir_operando(operando1, tipo_dato1, bits)
        # Convertir el segundo operando solo si es necesario
        operando2_valor = None
        if codop not in ["00111"]:  # Operaciones que no requieren segundo operando
            operando2_valor = self.__convertir_operando(operando2, tipo_dato2, bits)


        resultado = 0

        if codop == "00000":  # Suma
            resultado = operando1_valor + operando2_valor
        elif codop == "00001":  # Resta
            resultado = operando1_valor - operando2_valor
        elif codop == "00010":  # Multiplicación
            resultado = operando1_valor * operando2_valor
        elif codop == "00011":  # División
            if operando2_valor == 0:
                raise ZeroDivisionError("División por cero.")
            resultado = operando1_valor // operando2_valor
        elif codop == "00100":  # AND bit a bit
            resultado = operando1_valor & operando2_valor
        elif codop == "00101":  # OR bit a bit
            resultado = operando1_valor | operando2_valor
        elif codop == "00110":  # XOR bit a bit
            resultado = operando1_valor ^ operando2_valor
        elif codop == "00111":  # NOT bit a bit (solo operando1)
            resultado = ~operando1_valor & ((1 << bits) - 1)  # Asegurarse de que el resultado esté dentro del rango de bits
        else:
            raise ValueError(f"Código de operación no soportado: {codop}")

        # Guardar el resultado en binario
        self.__guardar_resultado(resultado, tipo_dato1, bits)

        # Actualizar los flags
        self.__actualizar_flags(resultado, tipo_dato1)

        return self.__resultado

    def __actualizar_flags(self, resultado: Union[int, float, bool], tipo_dato: str) -> None:
        if isinstance(resultado, (int, float)):
            self.__flags["ZERO"] = 1 if resultado == 0 else 0
            self.__flags["SIGN"] = 1 if resultado < 0 else 0
        else:
            self.__flags["ZERO"] = 0
            self.__flags["SIGN"] = 0

    def __binario_a_flotante(self, binario: str, bits: int = 48) -> float:
        signo = int(binario[0], 2)
        exponente = int(binario[1:12], 2) - 1023
        mantisa = binario[12:]
        valor_mantisa = 1 + sum(int(b) * 2 ** (-i) for i, b in enumerate(mantisa, start=1))
        return (-1) ** signo * valor_mantisa * 2 ** exponente

    def __flotante_a_binario(self, numero: float, bits: int = 48) -> str:
        if numero == 0:
            return "0" * bits
        signo = 0 if numero >= 0 else 1
        numero = abs(numero)
        exponente = math.floor(math.log2(numero))
        mantisa = numero / (2 ** exponente) - 1
        sesgo = 1023
        bits_exponente = f"{exponente + sesgo:011b}"
        bits_mantisa = ""
        for _ in range(bits - 12):
            mantisa *= 2
            if mantisa >= 1:
                bits_mantisa += "1"
                mantisa -= 1
            else:
                bits_mantisa += "0"
        return f"{signo}{bits_exponente}{bits_mantisa}"

    def obtener_operando1(self) -> str:
        return self.__operando1

    def obtener_operando2(self) -> str:
        return self.__operando2

    def obtener_codop(self) -> str:
        return self.__codop

    def obtener_resultado(self) -> str:
        return self.__resultado

    def obtener_flags(self) -> dict:
        return self.__flags