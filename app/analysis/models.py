from dataclasses import dataclass, field


@dataclass
class BudgetItem:
    """
    Represents a single item from a normalized budget.

    It contains the minimum information required
    for cost analysis.
    """

    code: str
    description: str
    unit: str

    quantity: float | None
    unit_price: float | None



@dataclass
class NormalizedBudget:
    """
    Represents a budget ready for analysis.

    The data has already passed through
    ingestion and normalization stages.
    """

    items: list[BudgetItem]
    source_filename: str


@dataclass
class ItemCost:
    """
    Represents the calculated cost
    of a budget item.
    """

    description: str
    quantity: float | None
    unit_price: float | None
    subtotal: float | None



@dataclass
class CostAnalysisResult:
    """
    Result of the cost analysis process.

    Contains:
    - individual item costs;
    - accumulated total cost.
    """

    item_costs: list[ItemCost]
    total_cost: float


@dataclass
class BudgetSummary:
    """
    Aggregated economic information
    about a budget analysis.
    """

    total_cost: float
    total_items: int
    calculated_items: int


@dataclass
class QualityIssue:
    """
    Represents a single detected problem
    in a budget item.
    """

    item_description: str
    issue_type: str
    message: str


@dataclass
class QualityReport:
    """
    Contains all detected quality issues
    from a budget analysis.
    """

    issues: list[QualityIssue] = field(
        default_factory=list
    )
