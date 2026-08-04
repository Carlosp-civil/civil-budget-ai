from pathlib import Path

import pandas as pd
from app.analysis.cost_analyzer import CostAnalyzer
from app.analysis.quality_analyzer import QualityAnalyzer
from app.ingestion.column_detector import ColumnDetector
from app.ingestion.models import BudgetDocument
from app.normalization.budget_normalizer import BudgetNormalizer
from app.normalization.domain_normalizer import DomainNormalizer
from app.pipeline import BudgetPipeline


def test_budget_pipeline_end_to_end():
    knowledge_path = Path(
        "data/knowledge/domain_aliases.json"
    )

    detector = ColumnDetector(
        DomainNormalizer(knowledge_path)
    )

    pipeline = BudgetPipeline(
        column_detector=detector,
        budget_normalizer=BudgetNormalizer(),
        cost_analyzer=CostAnalyzer(),
        quality_analyzer=QualityAnalyzer(),
    )

    dataframe = pd.DataFrame(
        {
            "Codigo": ["001"],
            "Descripcion": ["Concreto"],
            "Unidad": ["m3"],
            "Cantidad": [10],
            "Precio Unitario": [250000],
        }
    )

    document = BudgetDocument(
        data=dataframe,
        filename="budget.xlsx",
        columns=list(dataframe.columns),
    )

    result = pipeline.run(document)

    assert result.normalized_budget.source_filename == "budget.xlsx"

    assert result.cost_analysis.total_cost == 2_500_000

    assert result.quality_report.issues == []

    assert result.column_detection.mapping.codigo == "Codigo"
