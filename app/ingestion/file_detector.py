from enum import Enum
from pathlib import Path


class FileType(Enum):
    """
    Tipos de archivos soportados por el sistema.
    """

    EXCEL = "excel"
    CSV = "csv"


class FileDetector:
    """
    Detecta el tipo de archivo basado en su extensión.
    """

    def detect(
        self,
        file_path: str | Path
    ) -> FileType:
        """
        Determina el tipo de archivo.

        Args:
            file_path:
                Ruta del archivo.

        Returns:
            Tipo de archivo detectado.
        """

        extension = Path(file_path).suffix.lower()

        if extension in [".xlsx", ".xls"]:
            return FileType.EXCEL

        if extension == ".csv":
            return FileType.CSV

        raise ValueError(
            f"Formato de archivo no soportado: {extension}"
        )