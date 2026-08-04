# Context Prompt — Civil Budget AI Project

Estoy desarrollando un proyecto llamado **civil-budget-ai**.

## Descripción del proyecto

**Civil Budget AI** es una aplicación inteligente orientada al análisis automático de presupuestos de construcción (ingeniería civil).

El objetivo principal es permitir que un usuario cargue un archivo de presupuesto (principalmente Excel), y que el sistema sea capaz de:

1. Detectar automáticamente la estructura del archivo.
2. Identificar columnas aunque tengan diferentes nombres.
3. Normalizar la información usando conocimiento específico del dominio civil.
4. Convertir diferentes formatos de presupuestos a un modelo estándar.
5. Analizar costos.
6. Detectar problemas de calidad en los datos.
7. Generar reportes útiles para revisión técnica y toma de decisiones.

La visión final es crear una herramienta que ayude a ingenieros civiles, presupuestistas y empresas constructoras a revisar presupuestos más rápido y con menos errores.

---

# Arquitectura actual

El proyecto está organizado por módulos:

```
app/
│
├── ingestion/
│   ├── file_detector.py
│   ├── file_loader.py
│   ├── column_detector.py
│   └── models.py
│
├── normalization/
│   ├── text_normalizer.py
│   ├── domain_normalizer.py
│   ├── budget_normalizer.py
│   └── models.py
│
├── analysis/
│   ├── models.py
│   ├── cost_analyzer.py
│   ├── cost_summary_builder.py
│   └── quality_analyzer.py
│
├── knowledge/
│   └── domain_aliases.json
│
├── export/
│
└── ui/
```

---

# Lo que ya está construido

## 1. Ingestión de archivos

Implementado:

* detección de archivos;
* carga de archivos;
* modelos base para documentos de presupuesto.

Estado:
✅ funcional

---

## 2. Detección inteligente de columnas

Implementado:

* detección de columnas estándar:

  * codigo
  * descripcion
  * unidad
  * cantidad
  * precio_unitario

* soporte de alias:

Ejemplos:

```
Codigo
Cod
Código

Descripcion
Detalle

Unidad
Und

Cantidad
Cant

Precio Unitario
P.U.
```

* sistema de confianza:

```
high_confidence
medium_confidence
low_confidence
```

* resolución de conflictos cuando varias columnas pueden representar el mismo campo.

Estado:
✅ muy avanzado

---

## 3. Normalización de dominio civil

Implementado:

* normalizador de texto;
* normalizador basado en conocimiento;
* archivo de conocimiento:

```
data/knowledge/domain_aliases.json
```

Permite extender el sistema sin modificar código.

Estado:
✅ funcional

---

## 4. Modelo estándar de presupuesto

Implementado:

Entidades principales:

```python
BudgetItem

NormalizedBudget
```

Permiten representar cualquier presupuesto externo en una estructura común.

Estado:
✅ funcional

---

## 5. Análisis de costos

Implementado:

* análisis de costos;
* resumen de costos.

Estado:
✅ funcional básico

---

## 6. Control de calidad del presupuesto

Implementado:

`QualityAnalyzer`

Reglas actuales:

### Campos faltantes:

```
missing_quantity
missing_unit_price
missing_unit
```

### Valores inválidos:

```
invalid_quantity
invalid_unit_price
```

Ejemplos detectados:

```python
quantity=None

unit=None

quantity=0

unit_price=-50
```

Estado:
✅ funcional inicial

---

# Estado actual del proyecto

Última ejecución:

```
python -m pytest

30 passed
```

Todos los tests actuales están pasando.

El proyecto se encuentra aproximadamente en:

```
35-45% de un MVP funcional
```

La base arquitectónica está creada y validada.

---

# Próximo objetivo

La siguiente fase debe ser la integración completa del flujo.

Crear:

```
BudgetPipeline
```

que conecte:

```
Archivo Excel
      |
      v
FileLoader
      |
      v
ColumnDetector
      |
      v
BudgetNormalizer
      |
      v
CostAnalyzer
      |
      v
QualityAnalyzer
      |
      v
Reporte final
```

El objetivo será pasar de módulos independientes a una aplicación completa.

---

# Próximas fases después del pipeline

## Fase 1 — Integración

Crear:

```
app/pipeline/budget_pipeline.py
```

y pruebas:

```
tests/test_budget_pipeline.py
```

Debe permitir:

Entrada:

```
presupuesto.xlsx
```

Salida:

```
presupuesto normalizado
análisis de costos
reporte de calidad
```

---

## Fase 2 — Mejorar conocimiento civil

Ampliar:

```
domain_aliases.json
```

con:

* unidades civiles:

  * m2
  * m²
  * m3
  * m³
  * ml
  * und

* partidas comunes:

  * concreto
  * acero
  * excavación
  * relleno
  * formaleta

---

## Fase 3 — Exportación

Crear generación de:

* Excel limpio;
* reporte PDF;
* resumen ejecutivo.

---

## Fase 4 — Interfaz

Crear una UI donde el usuario pueda:

1. subir presupuesto;
2. revisar columnas detectadas;
3. confirmar normalización;
4. descargar resultados.

---

# Forma de trabajo

Continuar usando desarrollo incremental:

1. Crear test.
2. Ver fallo.
3. Implementar solución.
4. Ejecutar:

```
python -m pytest
```

5. Mantener todos los tests verdes.
6. Hacer commits pequeños y claros.

El proyecto debe mantener una arquitectura limpia, modular y orientada a producción.
