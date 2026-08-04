from pathlib import Path

from app.normalization.domain_normalizer import DomainNormalizer
from app.ingestion.column_detector import ColumnDetector


def test_detect_standard_columns():

    knowledge_path = Path(
        "data/knowledge/domain_aliases.json"
    )

    domain_normalizer = DomainNormalizer(
        knowledge_path
    )

    detector = ColumnDetector(
        domain_normalizer
    )

    columns = [
        "Codigo",
        "Descripcion",
        "Unidad",
        "Cantidad",
        "Precio Unitario"
    ]

    result = detector.detect(
        columns
    )

    assert result.mapping.codigo == "Codigo"
    assert result.mapping.descripcion == "Descripcion"
    assert result.mapping.unidad == "Unidad"
    assert result.mapping.cantidad == "Cantidad"
    assert result.mapping.precio_unitario == "Precio Unitario"

    assert result.warnings == []



def test_detect_alias_columns():

    knowledge_path = Path(
        "data/knowledge/domain_aliases.json"
    )

    domain_normalizer = DomainNormalizer(
        knowledge_path
    )

    detector = ColumnDetector(
        domain_normalizer
    )

    columns = [
        "Cod",
        "Detalle",
        "Und",
        "Cant",
        "P.U."
    ]

    result = detector.detect(
        columns
    )

    assert result.mapping.codigo == "Cod"
    assert result.mapping.descripcion == "Detalle"
    assert result.mapping.unidad == "Und"
    assert result.mapping.cantidad == "Cant"
    assert result.mapping.precio_unitario == "P.U."

    assert result.warnings == []



def test_ignore_unknown_columns():

    knowledge_path = Path(
        "data/knowledge/domain_aliases.json"
    )

    domain_normalizer = DomainNormalizer(
        knowledge_path
    )

    detector = ColumnDetector(
        domain_normalizer
    )

    columns = [
        "Fecha",
        "Proveedor",
        "Observaciones"
    ]

    result = detector.detect(
        columns
    )

    assert result.mapping.codigo is None
    assert result.mapping.descripcion is None
    assert result.mapping.unidad is None
    assert result.mapping.cantidad is None
    assert result.mapping.precio_unitario is None

    assert result.warnings == []

from app.normalization.models import NormalizationMatch


class FakeDomainNormalizer:

    def normalize(
        self,
        value: str,
        field_type: str
    ):

        if value == "P.U.":

            return [
                NormalizationMatch(
                    term="precio_unitario",
                    confidence="high_confidence"
                )
            ]

        if value == "Precio":

            return [
                NormalizationMatch(
                    term="precio_unitario",
                    confidence="medium_confidence"
                )
            ]

        return []



def test_detect_conflict_uses_highest_confidence():

    detector = ColumnDetector(
        FakeDomainNormalizer()
    )

    columns = [
        "P.U.",
        "Precio"
    ]

    result = detector.detect(
        columns
    )

    assert result.mapping.precio_unitario == "P.U."

    assert len(result.warnings) == 1