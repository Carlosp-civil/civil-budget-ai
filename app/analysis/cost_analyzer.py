from app.analysis.models import CostAnalysisResult, ItemCost, NormalizedBudget


class CostAnalyzer:
    """
    Calculates basic costs from a normalized budget.
    """


    def analyze(
        self,
        budget: NormalizedBudget
    ) -> CostAnalysisResult:

        item_costs = []

        total_cost = 0.0


        for item in budget.items:

            subtotal = self._calculate_subtotal(
                item.quantity,
                item.unit_price
            )


            if subtotal is not None:
                total_cost += subtotal


            item_costs.append(
                ItemCost(
                    description=item.description,
                    quantity=item.quantity,
                    unit_price=item.unit_price,
                    subtotal=subtotal
                )
            )


        return CostAnalysisResult(
            item_costs=item_costs,
            total_cost=total_cost
        )



    def _calculate_subtotal(
        self,
        quantity: float | None,
        unit_price: float | None
    ) -> float | None:
        """
        Calculates item subtotal only when
        required values exist.
        """

        if quantity is None:
            return None


        if unit_price is None:
            return None


        return quantity * unit_price