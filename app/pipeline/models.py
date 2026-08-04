from dataclasses import dataclass

from app.analysis.models import (
    CostAnalysisResult,
    NormalizedBudget,
    QualityReport,
)
from app.ingestion.models import ColumnDetectionResult


@dataclass(slots=True)
class PipelineResult:
    """
    Resultado completo del procesamiento
    de un presupuesto.

    Reúne la información generada por todas
    las etapas del pipeline.
    """

    normalized_budget: NormalizedBudget
    cost_analysis: CostAnalysisResult
    quality_report: QualityReport
    column_detection: ColumnDetectionResult
