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
        raise ValueError("The number of bits must be a positive integer.")

    try:
        numero_entero = int(numero)
    except ValueError:
        raise ValueError(f"'{numero}' is not a valid integer string.")

    valor_minimo = -(1 << (bits - 1))
    valor_maximo = (1 << (bits - 1)) - 1

    if not (valor_minimo <= numero_entero <= valor_maximo):
        raise ValueError(f"Number {numero_entero} cannot be represented in {bits} bits.")

    mascara = (1 << bits) - 1
    return "{:0{}b}".format(numero_entero & mascara, bits)
