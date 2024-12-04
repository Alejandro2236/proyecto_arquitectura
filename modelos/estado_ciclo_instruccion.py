from enum import Enum


class EstadoCicloInstruccion(Enum):
    FI = 1
    DI = 2
    CO = 3
    FO = 4
    EI = 5
    WO = 6
