from pathlib import Path

from app.analysis.analysis_engine import AnalysisEngine
from app.application.models import BudgetAnalysisResult
from app.ingestion.column_detector import ColumnDetector
from app.ingestion.file_loader import BudgetLoader
from app.normalization.budget_normalizer import BudgetNormalizer


class BudgetAnalysisService:
    """
    Orquesta el flujo completo de análisis.
    """

    def __init__(
        self,
        loader: BudgetLoader,
        detector: ColumnDetector,
        normalizer: BudgetNormalizer,
        engine: AnalysisEngine,
    ):
        self.loader = loader
        self.detector = detector
        self.normalizer = normalizer
        self.engine = engine

    def analyze(
        self,
        file_path: str | Path,
    ) -> BudgetAnalysisResult:

        document = self.loader.load(file_path)

        columns = self.detector.detect(document.columns)

        budget = self.normalizer.normalize(
            document,
            columns.mapping,
        )

        (
            cost,
            summary,
            quality,
        ) = self.engine.analyze(budget)

        return BudgetAnalysisResult(
            columns=columns,
            normalized_budget=budget,
            cost_analysis=cost,
            summary=summary,
            quality_report=quality,
        )
