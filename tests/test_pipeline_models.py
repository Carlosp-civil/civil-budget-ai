from app.analysis.models import (
    CostAnalysisResult,
    NormalizedBudget,
    QualityReport,
)
from app.ingestion.models import (
    ColumnDetectionResult,
    ColumnMapping,
)
from app.pipeline.models import PipelineResult


def test_pipeline_result_model():

    result = PipelineResult(
        normalized_budget=NormalizedBudget(
            items=[],
            source_filename="budget.xlsx",
        ),
        cost_analysis=CostAnalysisResult(
            item_costs=[],
            total_cost=0,
        ),
        quality_report=QualityReport(),
        column_detection=ColumnDetectionResult(
            mapping=ColumnMapping(),
            warnings=[],
        ),
    )

    assert result.normalized_budget.source_filename == "budget.xlsx"

    assert result.cost_analysis.total_cost == 0

    assert result.quality_report.issues == []

    assert result.column_detection.warnings == []
