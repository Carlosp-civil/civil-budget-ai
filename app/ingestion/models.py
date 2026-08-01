from dataclasses import dataclass, field

import pandas as pd


@dataclass
class BudgetDocument:
    """
    Representa un presupuesto cargado desde
    un archivo externo.

    Contiene la información necesaria para
    las siguientes etapas del procesamiento.
    """

    data: pd.DataFrame
    filename: str
    columns: list[str]


@dataclass
class ColumnMapping:
    codigo: str | None = None
    descripcion: str | None = None
    unidad: str | None = None
    cantidad: str | None = None
    precio_unitario: str | None = None


@dataclass
class ColumnDetectionResult:
    """
    Resultado completo de la detección
    automática de columnas.

    Contiene:
    - el mapeo encontrado;
    - advertencias generadas durante el proceso.
    """

    mapping: ColumnMapping
    warnings: list[str] = field(
        default_factory=list
    )