from pathlib import Path

from app.analysis.cost_analyzer import CostAnalyzer
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
        quality_analyzer: QualityAnalyzer,
    ):
        self.loader = loader
        self.detector = detector
        self.normalizer = normalizer
        self.cost_analyzer = cost_analyzer
        self.quality_analyzer = quality_analyzer

    def analyze(
        self,
        file_path: str | Path,
    ) -> BudgetAnalysisResult:

        document = self.loader.load(file_path)

        columns = self.detector.detect(document.columns)

        budget = self.normalizer.normalize(document, columns.mapping)

        cost = self.cost_analyzer.analyze(budget)

        quality = self.quality_analyzer.analyze(budget)

        return BudgetAnalysisResult(
            columns=columns,
            cost_analysis=cost,
            quality_report=quality,
        )
