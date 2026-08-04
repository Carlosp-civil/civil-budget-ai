"""
Civil Budget AI

Module:
    app.core.config

Description:
    Centralized application configuration.

This module defines the immutable configuration
used across the application.
"""

from dataclasses import dataclass


@dataclass(frozen=True, slots=True)
class AppConfig:
    """
    Global application configuration.

    Centralizes configurable values used by the
    different modules of Civil Budget AI.
    """

    # ------------------------------------------------------------------
    # File loading
    # ------------------------------------------------------------------

    default_excel_sheet: int = 0

    default_encoding: str = "utf-8"

    # ------------------------------------------------------------------
    # Numeric normalization
    # ------------------------------------------------------------------

    decimal_separator: str = "."

    thousands_separator: str = ","

    # ------------------------------------------------------------------
    # Export
    # ------------------------------------------------------------------

    export_directory: str = "exports"

    # ------------------------------------------------------------------
    # Application
    # ------------------------------------------------------------------

    debug: bool = False

    application_name: str = "Civil Budget AI"

    version: str = "0.6.1"


config = AppConfig()