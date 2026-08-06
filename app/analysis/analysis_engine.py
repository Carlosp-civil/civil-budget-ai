from app.analysis.cost_analyzer import CostAnalyzer
from app.analysis.cost_summary_builder import CostSummaryBuilder
from app.analysis.models import (
    BudgetSummary,
    CostAnalysisResult,
    NormalizedBudget,
    QualityReport,
)
from app.analysis.quality_analyzer import QualityAnalyzer


class AnalysisEngine:
    """
    Ejecuta todos los análisis sobre un presupuesto normalizado.
    """

    def __init__(
        self,
        cost_analyzer: CostAnalyzer,
        quality_analyzer: QualityAnalyzer,
        summary_builder: CostSummaryBuilder,
    ):
        self.cost_analyzer = cost_analyzer
        self.quality_analyzer = quality_analyzer
        self.summary_builder = summary_builder

    def analyze(
        self,
        budget: NormalizedBudget,
    ) -> tuple[
        CostAnalysisResult,
        BudgetSummary,
        QualityReport,
    ]:

        cost = self.cost_analyzer.analyze(budget)

        summary = self.summary_builder.build(cost)

        quality = self.quality_analyzer.analyze(budget)

        return (
            cost,
            summary,
            quality,
        )
