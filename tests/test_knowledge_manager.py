from app.normalization.domain_normalizer import DomainNormalizer


normalizer = DomainNormalizer(
    "data/knowledge/domain_aliases.json"
)


tests = [
    {
        "value": "UND",
        "field": "unidad"
    },
    {
        "value": "Cant.",
        "field": "cantidad"
    },
    {
        "value": "PU",
        "field": "precio_unitario"
    },
    {
        "value": "Concreto f'c=21 MPa",
        "field": "descripcion"
    }
]


for test in tests:

    results = normalizer.normalize(
        test["value"],
        test["field"]
    )

    print("\nEntrada:")
    print(test["value"])

    print("Campo:")
    print(test["field"])

    if not results:
        print("  Sin coincidencias")

    for result in results:
        print(
            f"  → {result.term} "
            f"({result.confidence})"
        )