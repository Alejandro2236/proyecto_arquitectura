import math


def transformar_int_en_complemento_a_dos(numero: str, bits: int) -> str:
    """
    Convierte un string que representa un número entero en su
    representación binaria de complemento a dos en formato string.

    :param numero: La representación binaria de la cadena del entero que se va a convertir.
    :type numero: str
    :param bits: El número de bits que se van a utilizar para la representación.
    :type bits: int
    :return: La representación binaria en complemento a dos del número entero como cadena.

    :raises ValueError: Si bits no es un entero positivo.
    :raises ValueError: Si numero no es un string entero válido.
    :raises ValueError: Si el valor entero de numero no puede representarse en el número de bits especificado.
    """

    if bits <= 0:
        raise ValueError("El número de bits debe ser un entero positivo.")

    try:
        numero_entero = int(numero)
    except ValueError:
        raise ValueError(f"'{numero}' no es un string entero válido.")

    valor_minimo = -(1 << (bits - 1))
    valor_maximo = (1 << (bits - 1)) - 1

    if not (valor_minimo <= numero_entero <= valor_maximo):
        raise ValueError(f"El número {numero_entero} no puede ser representado con {bits} bits.")

    mascara = (1 << bits) - 1
    return "{:0{}b}".format(numero_entero & mascara, bits)


def transformar_complemento_a_dos_en_int(binario: str) -> int:
    """
    Convierte una representación binaria en complemento a dos en formato string
    a un número entero en base 10, asumiendo que el número de bits es igual a
    la longitud de la cadena binaria.

    :param binario: La representación binaria del número en complemento a dos.
    :type binario: str
    :return: El número entero correspondiente en base 10.

    :raises ValueError: Si binario contiene caracteres no válidos.
    """

    bits = len(binario)

    try:
        valor_entero = int(binario, 2)
    except ValueError:
        raise ValueError(f"'{binario}' no es una cadena binaria válida.")

    if binario[0] == '1':
        valor_entero -= (1 << bits)

    return valor_entero


def transformar_float_en_formato_binario(numero: str, total_bits: int, cantidad_bits_exponente: int) -> str:
    if total_bits <= 0:
        raise ValueError("El número de bits debe ser un entero positivo.")

    if cantidad_bits_exponente <= 0:
        raise ValueError("El número de bits para exponente debe ser un entero positivo")

    try:
        numero_flotante: float = float(numero)
    except ValueError:
        raise ValueError(f"'{numero}' no es un string flotante válido.")

    if math.isclose(numero_flotante, 0.0, abs_tol=1e-09):
        return __obtener_bit_signo(numero_flotante) + "0" * (total_bits - 1)

    cantidad_bits_mantisa: int = total_bits - cantidad_bits_exponente - 1

    bit_signo: str = __obtener_bit_signo(numero_flotante)
    bits_exponente: str = __obtener_bits_exponente(numero_flotante, cantidad_bits_exponente)
    bits_mantisa: str = __obtener_bits_mantisa(numero_flotante, cantidad_bits_mantisa)

    return bit_signo + bits_exponente + bits_mantisa


def __obtener_bit_signo(numero_flotante: float) -> str:
    return "0" if numero_flotante >= 0 else "1"


def __obtener_bits_exponente(numero_flotante: float, cantidad_bits_exponente: int) -> str:
    exponente: int = math.floor(math.log2(abs(numero_flotante)))
    sesgo: int = (1 << (cantidad_bits_exponente - 1)) - 1
    exponente_corregido: int = exponente + sesgo

    if not (0 <= exponente_corregido < (1 << cantidad_bits_exponente)):
        raise ValueError(
            f"Exponente {exponente_corregido} fuera de rango para el formato {cantidad_bits_exponente} bits"
        )

    return f"{exponente_corregido:0{cantidad_bits_exponente}b}"


def __obtener_bits_mantisa(numero_flotante: float, cantidad_bits_mantisa: int) -> str:
    parte_fraccionaria: float = abs(numero_flotante) - 1
    bits_mantisa: str = ""

    for _ in range(cantidad_bits_mantisa):
        parte_fraccionaria *= 2
        if parte_fraccionaria >= 1:
            bits_mantisa += "1"
            parte_fraccionaria -= 1
        else:
            bits_mantisa += "0"

    return bits_mantisa[:cantidad_bits_mantisa]
