# Civil Budget AI - Architecture

## Overview

Civil Budget AI is an intelligent application for analyzing civil engineering construction budgets.

The system is designed around a modular architecture that separates the different stages of budget processing into independent components. This approach makes the application easier to test, extend, and maintain.

---

# High-Level Architecture

```
                   +----------------------+
                   |      UI / API        |
                   |  (Future Interface)  |
                   +----------+-----------+
                              |
                              v
                   +----------------------+
                   |      Pipeline        |
                   |  BudgetPipeline      |
                   +----------+-----------+
                              |
          +-------------------+-------------------+
          |                   |                   |
          v                   v                   v
 +----------------+   +----------------+   +----------------+
 |   Ingestion    |   | Normalization  |   |   Analysis     |
 +----------------+   +----------------+   +----------------+
          |                   |                   |
          +-------------------+-------------------+
                              |
                              v
                   +----------------------+
                   |      Knowledge       |
                   +----------------------+
                              |
                              v
                   +----------------------+
                   |         Core         |
                   +----------------------+
```

---

# Modules

## Core

Provides infrastructure shared across the application.

Responsibilities

- Application configuration
- Paths
- Exceptions
- Future utilities

---

## Ingestion

Responsible for loading external budget files.

Current responsibilities

- File detection
- File loading
- Column detection

Input

- Excel
- CSV

Output

- BudgetDocument

---

## Normalization

Transforms heterogeneous budgets into a standard internal representation.

Responsibilities

- Text normalization
- Domain normalization
- Budget normalization

Output

- NormalizedBudget

---

## Analysis

Performs calculations and quality validations.

Responsibilities

- Cost analysis
- Cost summaries
- Quality analysis

Output

- CostAnalysisResult
- QualityReport

---

## Knowledge

Contains civil engineering domain knowledge.

Examples

- Column aliases
- Units
- Construction terminology

Current source

```
knowledge/domain_aliases.json
```

---

## Pipeline (Future)

Will orchestrate the complete workflow.

```
Excel

↓

BudgetLoader

↓

ColumnDetector

↓

BudgetNormalizer

↓

CostAnalyzer

↓

QualityAnalyzer

↓

PipelineResult
```

---

## Export (Future)

Responsible for generating deliverables.

Examples

- Clean Excel
- PDF report
- Executive summary

---

## UI (Future)

User interface.

Responsibilities

- Upload budgets
- Confirm detected columns
- Review quality issues
- Download reports

---

# Dependency Rules

Dependencies must always point inward.

```
UI

↓

Pipeline

↓

Analysis

Normalization

Ingestion

↓

Knowledge

↓

Core
```

Modules must never depend on higher layers.

Example

✅ Allowed

Analysis → Core

Normalization → Core

Pipeline → Analysis

❌ Not Allowed

Analysis → UI

Knowledge → Pipeline

Core → Analysis

---

# Design Principles

The project follows these principles:

- Single Responsibility Principle (SRP)
- Open/Closed Principle (OCP)
- Dependency Inversion Principle (DIP)
- Composition over Inheritance
- Explicit Typing
- Testability
- Incremental Development

---

# Testing Strategy

Every feature must satisfy the following workflow.

```
Design

↓

Test

↓

Implementation

↓

Refactor

↓

Pytest

↓

Commit

↓

Push

↓

Release Tag
```

---

# Current Status

Current Release

```
v0.6.1
```

Approximate MVP completion

```
40%
```

Current Test Status

```
30 passed
```

---

# Future Evolution

Planned milestones

1. Complete processing pipeline.
2. Domain knowledge expansion.
3. Export engine.
4. Web interface.
5. AI-assisted recommendations.
6. Version 1.0 MVP.