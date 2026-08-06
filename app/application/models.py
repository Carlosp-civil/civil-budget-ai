from dataclasses import dataclass

from app.analysis.models import (
    BudgetSummary,
    CostAnalysisResult,
    NormalizedBudget,
    QualityReport,
)
from app.ingestion.models import ColumnDetectionResult


@dataclass
class BudgetAnalysisResult:
    """
    Resultado completo del análisis de un presupuesto.
    """

    columns: ColumnDetectionResult
    normalized_budget: NormalizedBudget
    cost_analysis: CostAnalysisResult
    summary: BudgetSummary
    quality_report: QualityReport
