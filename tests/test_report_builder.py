from app.analysis.models import (
    BudgetSummary,
    CostAnalysisResult,
    ItemCost,
    QualityReport,
)
from app.application.models import BudgetAnalysisResult
from app.ingestion.models import (
    ColumnDetectionResult,
    ColumnMapping,
)
from app.reporting.report_builder import ReportBuilder


def test_build_report():

    result = BudgetAnalysisResult(
        columns=ColumnDetectionResult(
            mapping=ColumnMapping(
                codigo="codigo",
                descripcion="descripcion",
                unidad="unidad",
                cantidad="cantidad",
                precio_unitario="precio_unitario",
            ),
            warnings=[],
        ),
        normalized_budget=None,
        cost_analysis=CostAnalysisResult(
            item_costs=[
                ItemCost(
                    description="Concreto",
                    quantity=10,
                    unit_price=250,
                    subtotal=2500,
                )
            ],
            total_cost=2500,
        ),
        summary=BudgetSummary(
            total_cost=2500,
            total_items=1,
            calculated_items=1,
        ),
        quality_report=QualityReport(),
    )

    builder = ReportBuilder()

    report = builder.build(result)

    assert report.data["summary"]["total_cost"] == 2500
    assert report.data["summary"]["total_items"] == 1
    assert report.data["summary"]["calculated_items"] == 1

    assert report.data["issues"] == []
