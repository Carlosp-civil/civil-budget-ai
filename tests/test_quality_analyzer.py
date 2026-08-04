from app.analysis.models import BudgetItem, NormalizedBudget
from app.analysis.quality_analyzer import QualityAnalyzer


def test_detect_missing_quantity():
    budget = NormalizedBudget(
        source_filename="test_budget.xlsx",
        items=[
            BudgetItem(
                code="001",
                description="Concrete",
                unit="m3",
                quantity=None,
                unit_price=100
            )
        ]
    )


    report = QualityAnalyzer().analyze(
        budget
    )


    assert len(report.issues) == 1

    assert report.issues[0].issue_type == (
        "missing_quantity"
    )




def test_detect_missing_unit_price():

    budget = NormalizedBudget(
        source_filename="test_budget.xlsx",
        items=[
            BudgetItem(
                code="001",
                description="Concrete",
                unit="m3",
                quantity=10,
                unit_price=None
            )
        ]
    )


    report = QualityAnalyzer().analyze(
        budget
    )


    assert len(report.issues) == 1

    assert report.issues[0].issue_type == (
        "missing_unit_price"
    )



def test_detect_missing_unit():

    budget = NormalizedBudget(
        source_filename="test_budget.xlsx",
        items=[
            BudgetItem(
                code="001",
                description="Concrete",
                unit=None,
                quantity=10,
                unit_price=100
            )
        ]
    )


    report = QualityAnalyzer().analyze(
        budget
    )


    assert len(report.issues) == 1

    assert report.issues[0].issue_type == (
        "missing_unit"
    )



def test_detect_invalid_quantity():

    budget = NormalizedBudget(
        source_filename="test_budget.xlsx",
        items=[
            BudgetItem(
                code="001",
                description="Concrete",
                unit="m3",
                quantity=0,
                unit_price=100
            )
        ]
    )


    report = QualityAnalyzer().analyze(
        budget
    )


    assert len(report.issues) == 1

    assert report.issues[0].issue_type == (
        "invalid_quantity"
    )



def test_detect_invalid_unit_price():

    budget = NormalizedBudget(
        source_filename="test_budget.xlsx",
        items=[
            BudgetItem(
                code="001",
                description="Concrete",
                unit="m3",
                quantity=10,
                unit_price=-50
            )
        ]
    )


    report = QualityAnalyzer().analyze(
        budget
    )


    assert len(report.issues) == 1

    assert report.issues[0].issue_type == (
        "invalid_unit_price"
    )