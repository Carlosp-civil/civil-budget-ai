from dataclasses import dataclass

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