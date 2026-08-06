from pathlib import Path

from app.analysis.cost_analyzer import CostAnalyzer
from app.analysis.cost_summary_builder import CostSummaryBuilder
from app.analysis.quality_analyzer import QualityAnalyzer
from app.application.models import BudgetAnalysisResult
from app.ingestion.column_detector import ColumnDetector
from app.ingestion.file_loader import BudgetLoader
from app.normalization.budget_normalizer import BudgetNormalizer


class BudgetAnalysisService:
    """
    Orquesta todo el proceso de análisis.
    """

    def __init__(
        self,
        loader: BudgetLoader,
        detector: ColumnDetector,
        normalizer: BudgetNormalizer,
        cost_analyzer: CostAnalyzer,
        summary_builder: CostSummaryBuilder,
        quality_analyzer: QualityAnalyzer,
    ):
        self.loader = loader
        self.detector = detector
        self.normalizer = normalizer
        self.cost_analyzer = cost_analyzer
        self.summary_builder = summary_builder
        self.quality_analyzer = quality_analyzer

    def analyze(
        self,
        file_path: str | Path,
    ) -> BudgetAnalysisResult:

        document = self.loader.load(file_path)

        columns = self.detector.detect(document.columns)

        budget = self.normalizer.normalize(document, columns.mapping)

        cost = self.cost_analyzer.analyze(budget)

        summary = self.summary_builder.build(cost)

        quality = self.quality_analyzer.analyze(budget)

        return BudgetAnalysisResult(
            columns=columns,
            normalized_budget=budget,
            cost_analysis=cost,
            summary=summary,
            quality_report=quality,
        )
