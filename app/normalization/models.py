from dataclasses import dataclass


@dataclass
class NormalizationMatch:
    """
    Representa una posible coincidencia encontrada
    durante un proceso de normalización.
    """

    term: str
    confidence: str