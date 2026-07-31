from app.ingestion.file_detector import FileDetector, FileType


def test_detect_excel_file():
    detector = FileDetector()

    result = detector.detect(
        "presupuesto.xlsx"
    )

    assert result == FileType.EXCEL


def test_detect_csv_file():
    detector = FileDetector()

    result = detector.detect(
        "presupuesto.csv"
    )

    assert result == FileType.CSV


def test_detect_unsupported_file():
    detector = FileDetector()

    try:
        detector.detect(
            "presupuesto.txt"
        )

        assert False

    except ValueError:
        assert True