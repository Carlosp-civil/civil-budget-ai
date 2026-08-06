from dataclasses import dataclass

from app.analysis.models import (
    CostAnalysisResult,
    QualityReport,
)
from app.ingestion.models import ColumnDetectionResult


@dataclass
class BudgetAnalysisResult:
    """
    Resultado completo del análisis de un presupuesto.
    """

    columns: ColumnDetectionResult
    cost_analysis: CostAnalysisResult
    quality_report: QualityReport
