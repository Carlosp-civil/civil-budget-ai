from app.analysis.models import (
    BudgetItem,
    NormalizedBudget
)

from app.analysis.cost_analyzer import (
    CostAnalyzer
)



def test_calculate_item_cost():

    budget = NormalizedBudget(
        items=[
            BudgetItem(
                code="001",
                description="Concrete",
                unit="m3",
                quantity=10,
                unit_price=200
            )
        ],
        source_filename="budget.xlsx"
    )


    result = CostAnalyzer().analyze(
        budget
    )


    item_cost = result.item_costs[0]


    assert item_cost.description == "Concrete"
    assert item_cost.subtotal == 2000



def test_calculate_total_cost():

    budget = NormalizedBudget(
        items=[
            BudgetItem(
                code="001",
                description="Concrete",
                unit="m3",
                quantity=10,
                unit_price=200
            ),
            BudgetItem(
                code="002",
                description="Steel",
                unit="kg",
                quantity=100,
                unit_price=5
            )
        ],
        source_filename="budget.xlsx"
    )


    result = CostAnalyzer().analyze(
        budget
    )


    assert result.total_cost == 2500



def test_keep_items_without_price():

    budget = NormalizedBudget(
        items=[
            BudgetItem(
                code="001",
                description="Sand",
                unit="m3",
                quantity=10,
                unit_price=None
            )
        ],
        source_filename="budget.xlsx"
    )


    result = CostAnalyzer().analyze(
        budget
    )


    item_cost = result.item_costs[0]


    assert item_cost.subtotal is None
    assert result.total_cost == 0