from app.analysis.models import (
    BudgetItem,
    NormalizedBudget
)


def test_create_budget_item():

    item = BudgetItem(
        code="001",
        description="Concrete f'c=21 MPa",
        unit="m3",
        quantity=10,
        unit_price=250
    )

    assert item.code == "001"
    assert item.description == "Concrete f'c=21 MPa"
    assert item.quantity == 10
    assert item.unit_price == 250



def test_budget_item_allows_missing_values():

    item = BudgetItem(
        code="002",
        description="Cement",
        unit="kg",
        quantity=None,
        unit_price=120
    )

    assert item.quantity is None



def test_create_normalized_budget():

    item = BudgetItem(
        code="001",
        description="Concrete",
        unit="m3",
        quantity=5,
        unit_price=200
    )


    budget = NormalizedBudget(
        items=[item],
        source_filename="budget.xlsx"
    )


    assert len(budget.items) == 1
    assert budget.source_filename == "budget.xlsx"