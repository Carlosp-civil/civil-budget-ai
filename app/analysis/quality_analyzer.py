from app.analysis.models import (
    NormalizedBudget,
    QualityIssue,
    QualityReport
)


class QualityAnalyzer:
    """
    Detects quality problems in a normalized budget.
    """


    def analyze(
        self,
        budget: NormalizedBudget
    ) -> QualityReport:
        """
        Runs all quality validation rules.
        """

        issues = []


        issues.extend(
            self._check_missing_quantity(
                budget
            )
        )


        issues.extend(
            self._check_missing_unit_price(
                budget
            )
        )


        issues.extend(
            self._check_missing_unit(
                budget
            )
        )


        return QualityReport(
            issues=issues
        )


    def _check_missing_quantity(
        self,
        budget: NormalizedBudget
    ) -> list[QualityIssue]:
        """
        Detects budget items without quantity.
        """

        issues = []


        for item in budget.items:

            if item.quantity is None:

                issues.append(
                    QualityIssue(
                        item_description=item.description,
                        issue_type="missing_quantity",
                        message="Quantity is missing"
                    )
                )


        return issues


    def _check_missing_unit_price(
        self,
        budget: NormalizedBudget
    ) -> list[QualityIssue]:
        """
        Detects budget items without unit price.
        """

        issues = []


        for item in budget.items:

            if item.unit_price is None:

                issues.append(
                    QualityIssue(
                        item_description=item.description,
                        issue_type="missing_unit_price",
                        message="Unit price is missing"
                    )
                )


        return issues


    def _check_missing_unit(
        self,
        budget: NormalizedBudget
    ) -> list[QualityIssue]:
        """
        Detects budget items without measurement unit.
        """

        issues = []


        for item in budget.items:

            if not item.unit:

                issues.append(
                    QualityIssue(
                        item_description=item.description,
                        issue_type="missing_unit",
                        message="Unit is missing"
                    )
                )


        return issues