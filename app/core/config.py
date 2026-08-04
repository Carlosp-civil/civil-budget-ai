"""
Civil Budget AI

Module:
    core.config

Description:
    Centralized application configuration.
"""

from dataclasses import dataclass


@dataclass(frozen=True)
class AppConfig:
    """
    Global application configuration.

    This class centralizes configurable values used
    across the application.
    """

    # File loading

    default_excel_sheet: int = 0

    default_encoding: str = "utf-8"

    # Numeric processing

    decimal_separator: str = "."

    thousands_separator: str = ","

    # Export

    export_directory: str = "outputs"

    # Future options

    debug: bool = False


config = AppConfig()