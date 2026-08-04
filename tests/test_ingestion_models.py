from app.ingestion.models import ColumnCandidate, ColumnDetectionResult, ColumnMapping


def test_column_candidate_creation():

    candidate = ColumnCandidate(
        column_name="P.U.",
        field="precio_unitario",
        confidence="high_confidence",
        source="domain_alias"
    )

    assert candidate.column_name == "P.U."
    assert candidate.field == "precio_unitario"
    assert candidate.confidence == "high_confidence"
    assert candidate.source == "domain_alias"



def test_column_detection_result_contains_mapping():

    mapping = ColumnMapping(
        codigo="Codigo",
        cantidad="Cantidad"
    )

    result = ColumnDetectionResult(
        mapping=mapping
    )

    assert result.mapping.codigo == "Codigo"
    assert result.mapping.cantidad == "Cantidad"
    assert result.warnings == []