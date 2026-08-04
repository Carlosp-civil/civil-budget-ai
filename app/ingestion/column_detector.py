from collections import defaultdict

from app.ingestion.models import ColumnCandidate, ColumnDetectionResult, ColumnMapping
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

    CONFIDENCE_PRIORITY = {
        "high_confidence": 3,
        "medium_confidence": 2,
        "low_confidence": 1,
    }


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

        candidates = self._collect_raw_matches(
            columns
        )

        return self._resolve_conflicts(
            candidates
        )


    def _collect_raw_matches(
        self,
        columns: list[str]
    ) -> list[ColumnCandidate]:
        """
        Recolecta posibles interpretaciones
        de las columnas sin tomar decisiones finales.
        """

        candidates = []


        for column in columns:

            for field in self.TARGET_FIELDS:

                matches = self.domain_normalizer.normalize(
                    column,
                    field
                )


                for match in matches:

                    candidates.append(
                        ColumnCandidate(
                            column_name=column,
                            field=match.term,
                            confidence=match.confidence,
                            source="domain_alias"
                        )
                    )


        return candidates


    def _resolve_conflicts(
        self,
        candidates: list[ColumnCandidate]
    ) -> ColumnDetectionResult:
        """
        Resuelve múltiples candidatos para un mismo campo.

        Reglas:
        1. Mayor nivel de confianza gana.
        2. Si hay empate, gana la primera aparición.
        """

        mapping = ColumnMapping()

        warnings = []


        grouped_candidates = defaultdict(list)


        for candidate in candidates:

            grouped_candidates[
                candidate.field
            ].append(
                candidate
            )


        for field, field_candidates in grouped_candidates.items():

            unique_columns = list(
                dict.fromkeys(
                    candidate.column_name
                    for candidate in field_candidates
                )
            )


            if len(unique_columns) > 1:

                column_names = ", ".join(
                    unique_columns
                )

                warnings.append(
                    f"Multiple candidates found for field '{field}': {column_names}"
                )

            winner = max(
                field_candidates,
                key=lambda candidate: (
                    self.CONFIDENCE_PRIORITY.get(
                        candidate.confidence,
                        0
                    ),
                    -field_candidates.index(candidate)
                )
            )


            setattr(
                mapping,
                field,
                winner.column_name
            )


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