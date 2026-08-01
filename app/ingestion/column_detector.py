from app.ingestion.models import (
    ColumnDetectionResult,
    ColumnMapping
)

from app.normalization.domain_normalizer import DomainNormalizer


class ColumnDetector:
    """
    Detecta columnas de un presupuesto
    utilizando conocimiento del dominio.
    """

    TARGET_FIELDS = [
        "codigo",
        "descripcion",
        "unidad",
        "cantidad",
        "precio_unitario"
    ]


    def __init__(
        self,
        domain_normalizer: DomainNormalizer
    ):
        self.domain_normalizer = domain_normalizer


    def detect(
        self,
        columns: list[str]
    ) -> ColumnDetectionResult:
        """
        Analiza nombres de columnas y devuelve
        un resultado con mapeo y advertencias.
        """

        mapping = ColumnMapping()

        warnings = []


        for column in columns:

            for field in self.TARGET_FIELDS:

                matches = self.domain_normalizer.normalize(
                    column,
                    field
                )

                if matches:

                    self._assign_match(
                        mapping,
                        matches[0].term,
                        column
                    )

                    break


        return ColumnDetectionResult(
            mapping=mapping,
            warnings=warnings
        )


    def _assign_match(
        self,
        mapping: ColumnMapping,
        field: str,
        column_name: str
    ) -> None:
        """
        Asigna una columna detectada al campo correspondiente.
        """

        setattr(
            mapping,
            field,
            column_name
        )