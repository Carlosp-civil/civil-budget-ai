from app.analysis.cost_analyzer import CostAnalyzer
from app.analysis.quality_analyzer import QualityAnalyzer
from app.ingestion.column_detector import ColumnDetector
from app.ingestion.models import BudgetDocument
from app.normalization.budget_normalizer import BudgetNormalizer
from app.pipeline.models import PipelineResult


class BudgetPipeline:
    """
    Orquesta todo el procesamiento de un presupuesto.
    """

    def __init__(
        self,
        column_detector: ColumnDetector,
        budget_normalizer: BudgetNormalizer,
        cost_analyzer: CostAnalyzer,
        quality_analyzer: QualityAnalyzer,
    ):
        self.column_detector = column_detector
        self.budget_normalizer = budget_normalizer
        self.cost_analyzer = cost_analyzer
        self.quality_analyzer = quality_analyzer

    def run(
        self,
        document: BudgetDocument,
    ) -> PipelineResult:
        """
        Ejecuta el flujo completo sobre un BudgetDocument.
        """

        column_detection = self.column_detector.detect(
            document.columns
        )

        normalized_budget = self.budget_normalizer.normalize(
            document,
            column_detection.mapping,
        )

        cost_analysis = self.cost_analyzer.analyze(
            normalized_budget
        )

        quality_report = self.quality_analyzer.analyze(
            normalized_budget
        )

        return PipelineResult(
            normalized_budget=normalized_budget,
            cost_analysis=cost_analysis,
            quality_report=quality_report,
            column_detection=column_detection,
        )
