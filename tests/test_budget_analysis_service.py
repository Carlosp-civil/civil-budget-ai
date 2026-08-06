from pathlib import Path

import pandas as pd
from app.analysis.cost_analyzer import CostAnalyzer
from app.analysis.quality_analyzer import QualityAnalyzer
from app.application.budget_analysis_service import BudgetAnalysisService
from app.ingestion.column_detector import ColumnDetector
from app.ingestion.file_detector import FileDetector
from app.ingestion.file_loader import BudgetLoader
from app.normalization.budget_normalizer import BudgetNormalizer
from app.normalization.domain_normalizer import DomainNormalizer


def test_budget_analysis_service(tmp_path):
    csv_file = tmp_path / "budget.csv"

    dataframe = pd.DataFrame(
        {
            "codigo": ["001"],
            "descripcion": ["Concreto"],
            "unidad": ["m3"],
            "cantidad": [10],
            "precio_unitario": [250],
        }
    )

    dataframe.to_csv(csv_file, index=False)

    loader = BudgetLoader(FileDetector())

    detector = ColumnDetector(
        DomainNormalizer(Path("data/knowledge/domain_aliases.json"))
    )

    service = BudgetAnalysisService(
        loader=loader,
        detector=detector,
        normalizer=BudgetNormalizer(),
        cost_analyzer=CostAnalyzer(),
        quality_analyzer=QualityAnalyzer(),
    )

    document = loader.load(csv_file)

    print(document.columns)

    detection = detector.detect(document.columns)

    print(detection.mapping)

    result = service.analyze(csv_file)

    assert result.cost_analysis.total_cost == 2500

    assert len(result.quality_report.issues) == 0

    assert result.columns.mapping.codigo == "codigo"
