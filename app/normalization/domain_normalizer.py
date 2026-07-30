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


        return self._sort_by_confidence(
            matches
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
        Ordena resultados:
        primero alta confianza,
        luego baja confianza.
        """

        priority = {
            "high_confidence": 0,
            "low_confidence": 1
        }


        return sorted(
            matches,
            key=lambda match: priority.get(
                match.confidence,
                99
            )
        )