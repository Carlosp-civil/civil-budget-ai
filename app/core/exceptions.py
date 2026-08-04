"""
Civil Budget AI

Module:
    app.core.exceptions

Description:
    Base exception hierarchy for the application.
"""

from dataclasses import dataclass
from typing import Any


@dataclass(slots=True)
class ErrorContext:
    """
    Additional information associated with an application error.
    """

    details: str | None = None
    metadata: dict[str, Any] | None = None


class CivilBudgetError(Exception):
    """
    Base exception for all application-specific errors.
    """

    def __init__(
        self,
        message: str,
        context: ErrorContext | None = None,
    ) -> None:
        super().__init__(message)
        self.message = message
        self.context = context

    def __str__(self) -> str:
        if self.context and self.context.details:
            return f"{self.message} ({self.context.details})"

        return self.message


class ConfigurationError(CivilBudgetError):
    """
    Raised when the application configuration is invalid.
    """


class IngestionError(CivilBudgetError):
    """
    Raised during file loading or ingestion.
    """


class AnalysisError(CivilBudgetError):
    """
    Raised during analysis operations.
    """