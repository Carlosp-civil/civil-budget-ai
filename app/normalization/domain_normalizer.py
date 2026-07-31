import json
from pathlib import Path
from typing import Dict, List

from app.normalization.text_normalizer import TextNormalizer
from app.normalization.models import NormalizationMatch


class DomainNormalizer:
    """
    Normaliza términos utilizando conocimiento específico
    del dominio de Ingeniería Civil.

    Permite:
    - múltiples coincidencias;
    - niveles de confianza;
    - reglas diferentes según el tipo de campo.
    """

    # Campos donde los caracteres técnicos tienen significado.
    # Ejemplo:
    # f'c=21 MPa
    # kg/cm²
    # Ø4"
    CONSERVATIVE_FIELDS = {
        "unidad",
        "descripcion"
    }

    _CONFIDENCE_PRIORITY = {
        "high_confidence": 3,
        "medium_confidence": 2,
        "low_confidence": 1,
    }


    def __init__(
        self,
        knowledge_path: str | Path
    ):
        self.knowledge_path = Path(
            knowledge_path
        )

        self.text_normalizer = TextNormalizer()

        """
        Estructura interna:

        {
            "und": [
                NormalizationMatch(
                    term="unidad",
                    confidence="high_confidence"
                )
            ]
        }

        Un alias puede tener múltiples resultados.
        """

        self.alias_map: Dict[
            str,
            List[NormalizationMatch]
        ] = {}

        self.load()


    def load(self) -> None:
        """
        Carga el conocimiento del dominio
        y construye el mapa invertido de búsqueda.
        """

        if not self.knowledge_path.exists():
            raise FileNotFoundError(
                f"No se encontró el archivo: {self.knowledge_path}"
            )


        with open(
            self.knowledge_path,
            "r",
            encoding="utf-8"
        ) as file:

            knowledge = json.load(file)


        self.alias_map = {}


        for standard_term, confidence_levels in knowledge.items():

            for confidence, aliases in confidence_levels.items():

                for alias in aliases:

                    normalized_alias = (
                        self._normalize_value(
                            alias,
                            standard_term
                        )
                    )


                    match = NormalizationMatch(
                        term=standard_term,
                        confidence=confidence
                    )


                    if normalized_alias not in self.alias_map:
                        self.alias_map[normalized_alias] = []


                    self.alias_map[normalized_alias].append(
                        match
                    )


    def normalize(
        self,
        value: str,
        field_type: str
    ) -> List[NormalizationMatch]:
        """
        Busca posibles equivalencias para un valor.

        Args:
            value:
                Texto ingresado por el usuario.

            field_type:
                Tipo de campo del presupuesto.
                Ej:
                codigo
                descripcion
                unidad
                cantidad
                precio_unitario

        Returns:
            Lista de posibles coincidencias
            ordenadas por confianza.
        """

        if not value:
            return []

        normalized_value = (
            self._normalize_value(
                value,
                field_type
            )
        )

        matches = self.alias_map.get(
            normalized_value,
            []
        )

        best_matches = self._select_best_matches(
            matches
        )

        return self._sort_by_confidence(
            best_matches
        )


    def _normalize_value(
        self,
        value: str,
        field_type: str
    ) -> str:
        """
        Decide qué estrategia de normalización aplicar
        dependiendo del tipo de campo.
        """

        preserve_special_chars = (
            field_type in self.CONSERVATIVE_FIELDS
        )


        return self.text_normalizer.normalize(
            value,
            preserve_special_chars=preserve_special_chars
        )


    def _sort_by_confidence(
        self,
        matches: List[NormalizationMatch]
    ) -> List[NormalizationMatch]:
        """
        Ordena las coincidencias desde la mayor
        hasta la menor confianza.
        """

        return sorted(
            matches,
            key=lambda match: self._CONFIDENCE_PRIORITY.get(
                match.confidence,
                0
            ),
            reverse=True
        )

    def _select_best_matches(
        self,
        matches: List[NormalizationMatch],
    ) -> List[NormalizationMatch]:
        """
        Retorna únicamente la coincidencia con mayor confianza para cada
        término canónico.
        """

        best_matches: Dict[str, NormalizationMatch] = {}

        for match in matches:
            if match.term not in best_matches:
                best_matches[match.term] = match
                continue

            current_match = best_matches[match.term]

            current_priority = self._CONFIDENCE_PRIORITY.get(
                current_match.confidence,
                0
            )

            new_priority = self._CONFIDENCE_PRIORITY.get(
                match.confidence,
                0
            )

            if new_priority > current_priority:
                best_matches[match.term] = match

        return list(best_matches.values())