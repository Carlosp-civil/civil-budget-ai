import pandas as pd
from app.ingestion.models import BudgetDocument, ColumnMapping
from app.normalization.budget_normalizer import BudgetNormalizer


def create_document(data):

    return BudgetDocument(
        data=pd.DataFrame(data),
        filename="budget.xlsx",
        columns=list(data.keys())
    )



def test_normalize_valid_budget():

    document = create_document(
        {
            "Codigo": ["001"],
            "Descripcion": ["Cemento"],
            "Unidad": ["kg"],
            "Cantidad": ["100"],
            "Precio": ["120"]
        }
    )


    mapping = ColumnMapping(
        codigo="Codigo",
        descripcion="Descripcion",
        unidad="Unidad",
        cantidad="Cantidad",
        precio_unitario="Precio"
    )


    normalizer = BudgetNormalizer()


    result = normalizer.normalize(
        document,
        mapping
    )


    item = result.items[0]

    assert item.code == "001"
    assert item.description == "Cemento"
    assert item.quantity == 100.0
    assert item.unit_price == 120.0



def test_normalize_missing_values():

    document = create_document(
        {
            "Codigo": ["002"],
            "Descripcion": ["Arena"],
            "Unidad": ["m3"],
            "Cantidad": [None],
            "Precio": ["50"]
        }
    )


    mapping = ColumnMapping(
        codigo="Codigo",
        descripcion="Descripcion",
        unidad="Unidad",
        cantidad="Cantidad",
        precio_unitario="Precio"
    )


    result = BudgetNormalizer().normalize(
        document,
        mapping
    )


    item = result.items[0]


    assert item.quantity is None
    assert item.unit_price == 50.0



def test_ignore_empty_rows():

    document = create_document(
        {
            "Codigo": ["001", None],
            "Descripcion": ["Cemento", None],
            "Unidad": ["kg", None],
            "Cantidad": ["100", None],
            "Precio": ["120", None]
        }
    )


    mapping = ColumnMapping(
        codigo="Codigo",
        descripcion="Descripcion",
        unidad="Unidad",
        cantidad="Cantidad",
        precio_unitario="Precio"
    )


    result = BudgetNormalizer().normalize(
        document,
        mapping
    )


    assert len(result.items) == 1