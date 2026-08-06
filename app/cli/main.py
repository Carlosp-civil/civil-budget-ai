from argparse import ArgumentParser
from pathlib import Path

from app.analysis.analysis_engine import AnalysisEngine
from app.analysis.cost_analyzer import CostAnalyzer
from app.analysis.cost_summary_builder import CostSummaryBuilder
from app.analysis.quality_analyzer import QualityAnalyzer
from app.application.budget_analysis_service import BudgetAnalysisService
from app.ingestion.column_detector import ColumnDetector
from app.ingestion.file_detector import FileDetector
from app.ingestion.file_loader import BudgetLoader
from app.normalization.budget_normalizer import BudgetNormalizer
from app.normalization.domain_normalizer import DomainNormalizer
from app.reporting.report_builder import ReportBuilder


def build_service() -> BudgetAnalysisService:
    """
    Construye todas las dependencias de la aplicación.
    """

    loader = BudgetLoader(FileDetector())

    detector = ColumnDetector(
        DomainNormalizer(Path("data/knowledge/domain_aliases.json"))
    )

    engine = AnalysisEngine(
        cost_analyzer=CostAnalyzer(),
        quality_analyzer=QualityAnalyzer(),
        summary_builder=CostSummaryBuilder(),
    )

    return BudgetAnalysisService(
        loader=loader,
        detector=detector,
        normalizer=BudgetNormalizer(),
        engine=engine,
    )


def main() -> None:

    parser = ArgumentParser(prog="budget-ai", description="Civil Budget AI")

    parser.add_argument("file", help="Archivo Excel o CSV")

    args = parser.parse_args()

    service = build_service()

    result = service.analyze(args.file)

    report = ReportBuilder().build(result)

    print("=" * 50)
    print("Civil Budget AI")
    print("=" * 50)
    print()

    print(f"Archivo: {args.file}")
    print()

    print("Resumen")
    print("-" * 20)

    summary = report.data["summary"]

    print(f"Total costo      : {summary['total_cost']}")
    print(f"Items            : {summary['total_items']}")
    print(f"Calculados       : {summary['calculated_items']}")

    print()

    print("Problemas")

    if report.data["issues"]:
        for issue in report.data["issues"]:
            print(f"- {issue}")

    else:
        print("Ninguno")


if __name__ == "__main__":
    main()
