from app.analysis.models import (
    ItemCost,
    CostAnalysisResult
)

from app.analysis.cost_summary_builder import (
    CostSummaryBuilder
)



def test_build_budget_summary():

    analysis = CostAnalysisResult(
        item_costs=[
            ItemCost(
                description="Concrete",
                quantity=10,
                unit_price=200,
                subtotal=2000
            ),
            ItemCost(
                description="Steel",
                quantity=100,
                unit_price=5,
                subtotal=500
            )
        ],
        total_cost=2500
    )


    summary = CostSummaryBuilder().build(
        analysis
    )


    assert summary.total_cost == 2500
    assert summary.total_items == 2
    assert summary.calculated_items == 2



def test_summary_counts_missing_cost_items():

    analysis = CostAnalysisResult(
        item_costs=[
            ItemCost(
                description="Sand",
                quantity=10,
                unit_price=None,
                subtotal=None
            )
        ],
        total_cost=0
    )


    summary = CostSummaryBuilder().build(
        analysis
    )


    assert summary.total_items == 1
    assert summary.calculated_items == 0