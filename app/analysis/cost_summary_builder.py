from app.analysis.models import (
    BudgetSummary,
    CostAnalysisResult
)


class CostSummaryBuilder:
    """
    Builds aggregated information from
    a cost analysis result.
    """


    def build(
        self,
        analysis_result: CostAnalysisResult
    ) -> BudgetSummary:
        """
        Creates an economic summary
        from calculated item costs.
        """

        calculated_items = 0


        for item_cost in analysis_result.item_costs:

            if item_cost.subtotal is not None:
                calculated_items += 1


        return BudgetSummary(
            total_cost=analysis_result.total_cost,
            total_items=len(
                analysis_result.item_costs
            ),
            calculated_items=calculated_items
        )