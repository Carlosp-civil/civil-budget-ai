from app.application.models import BudgetAnalysisResult
from app.reporting.models import Report


class ReportBuilder:
    """
    Convierte el resultado del análisis
    en una estructura serializable.
    """

    def build(
        self,
        result: BudgetAnalysisResult,
    ) -> Report:

        return Report(
            data={
                "summary": {
                    "total_cost": result.summary.total_cost,
                    "total_items": result.summary.total_items,
                    "calculated_items": result.summary.calculated_items,
                },
                "issues": [
                    {
                        "item": issue.item_description,
                        "type": issue.issue_type,
                        "message": issue.message,
                    }
                    for issue in result.quality_report.issues
                ],
            }
        )
