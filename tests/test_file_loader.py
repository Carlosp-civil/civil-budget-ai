import pandas as pd
import pytest

from app.ingestion.file_detector import FileDetector
from app.ingestion.file_loader import BudgetLoader
from app.ingestion.models import BudgetDocument


def test_load_csv_file(tmp_path):
    csv_file = tmp_path / "budget.csv"

    csv_file.write_text(
        "codigo,descripcion,cantidad\n"
        "001,Concreto,10\n",
        encoding="utf-8"
    )


    loader = BudgetLoader(
        FileDetector()
    )


    document = loader.load(
        csv_file
    )


    assert isinstance(
        document,
        BudgetDocument
    )

    assert document.filename == "budget.csv"

    assert document.columns == [
        "codigo",
        "descripcion",
        "cantidad"
    ]

    assert len(document.data) == 1



def test_load_non_existing_file():

    loader = BudgetLoader(
        FileDetector()
    )


    with pytest.raises(
        FileNotFoundError
    ):
        loader.load(
            "archivo_inexistente.csv"
        )