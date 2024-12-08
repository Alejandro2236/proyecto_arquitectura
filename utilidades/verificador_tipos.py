def es_int(operando: str) -> bool:
    if not operando.isdigit():
        if not (operando.startswith("-") and operando[1:].isdigit()):
            return False
    return True


def es_float(operando: str) -> bool:
    try:
        float(operando)
        if "." not in operando:
            return False
        return True
    except ValueError:
        return False


def es_registro(operando: str) -> bool:
    if not operando.startswith('R'):
        return False
    if not operando[1:].isdigit():
        return False
    return True


def es_direccion_memoria(operando: str) -> bool:
    if not operando.startswith("#"):
        return False
    if not operando[1:].isdigit():
        return False
    return True


def es_etiqueta(operando: str) -> bool:
    if len(operando.split()) != 1:
        return False
    if not operando.endswith(":"):
        return False
    if not operando[:-1].isalpha():
        return False
    return True

