from pathlib import Path

import pandas as pd

from app.ingestion.file_detector import FileDetector, FileType
from app.ingestion.models import BudgetDocument


class BudgetLoader:
    """
    Carga archivos de presupuesto y los convierte
    en un BudgetDocument.
    """

    def __init__(
        self,
        file_detector: FileDetector
    ):
        self.file_detector = file_detector


    def load(
        self,
        file_path: str | Path
    ) -> BudgetDocument:
        """
        Carga un archivo de presupuesto.

        Args:
            file_path:
                Ruta del archivo.

        Returns:
            BudgetDocument con los datos cargados.
        """

        path = Path(file_path)

        if not path.exists():
            raise FileNotFoundError(
                f"No existe el archivo: {path}"
            )


        file_type = self.file_detector.detect(
            path
        )


        if file_type == FileType.EXCEL:
            data = self._load_excel(
                path
            )

        elif file_type == FileType.CSV:
            data = self._load_csv(
                path
            )

        else:
            raise ValueError(
                "Tipo de archivo no soportado"
            )


        return BudgetDocument(
            data=data,
            filename=path.name,
            columns=list(data.columns)
        )


    def _load_excel(
        self,
        path: Path
    ) -> pd.DataFrame:
        """
        Carga archivos Excel.
        """

        try:
            return pd.read_excel(
                path
            )

        except Exception as error:
            raise ValueError(
                f"No fue posible leer Excel: {error}"
            )


    def _load_csv(
        self,
        path: Path
    ) -> pd.DataFrame:
        """
        Carga archivos CSV.
        """

        try:
            return pd.read_csv(
                path
            )

        except Exception as error:
            raise ValueError(
                f"No fue posible leer CSV: {error}"
            )