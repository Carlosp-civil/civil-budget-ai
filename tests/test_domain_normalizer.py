from app.normalization.domain_normalizer import DomainNormalizer
from app.normalization.models import NormalizationMatch


def test_select_best_match_keeps_highest_confidence():
    normalizer = DomainNormalizer.__new__(DomainNormalizer)

    matches = [
        NormalizationMatch(
            term="precio_unitario",
            confidence="low_confidence"
        ),
        NormalizationMatch(
            term="precio_unitario",
            confidence="high_confidence"
        ),
    ]

    result = normalizer._select_best_matches(matches)

    assert len(result) == 1
    assert result[0].term == "precio_unitario"
    assert result[0].confidence == "high_confidence"


def test_select_best_matches_keeps_different_terms():
    normalizer = DomainNormalizer.__new__(DomainNormalizer)

    matches = [
        NormalizationMatch(
            term="unidad",
            confidence="high_confidence"
        ),
        NormalizationMatch(
            term="cantidad",
            confidence="medium_confidence"
        ),
    ]

    result = normalizer._select_best_matches(matches)

    assert len(result) == 2
    assert result[0].term == "unidad"
    assert result[1].term == "cantidad"


def test_select_best_matches_removes_same_confidence_duplicates():
    normalizer = DomainNormalizer.__new__(DomainNormalizer)

    matches = [
        NormalizationMatch(
            term="unidad",
            confidence="high_confidence"
        ),
        NormalizationMatch(
            term="unidad",
            confidence="high_confidence"
        ),
    ]

    result = normalizer._select_best_matches(matches)

    assert len(result) == 1
    assert result[0].term == "unidad"
    assert result[0].confidence == "high_confidence"