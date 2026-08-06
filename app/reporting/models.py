from dataclasses import dataclass
from typing import Any


@dataclass
class Report:
    """
    Representa un reporte generado
    a partir de un análisis de presupuesto.
    """

    data: dict[str, Any]
