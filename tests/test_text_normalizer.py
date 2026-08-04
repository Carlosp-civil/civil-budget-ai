from app.normalization.text_normalizer import TextNormalizer

normalizer = TextNormalizer()


tests = [
    ("Concreto f'c=21 MPa", True),
    ("kg/cm²", True),
    ("Cant.", False),
    ("Descripción.", False)
]


for text, preserve in tests:

    result = normalizer.normalize(
        text,
        preserve_special_chars=preserve
    )

    print(
        text,
        "->",
        result
    )