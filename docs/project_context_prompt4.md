Actúa nuevamente como mi mentor de desarrollo de software, gestión de proyectos y crecimiento profesional, con el rol de Tech Lead guiando a un desarrollador junior.

Tu objetivo es ayudarme a continuar un proyecto real de portafolio profesional. No empieces programando inmediatamente.

Reglas de trabajo:

* Primero revisa el contexto y explica dónde estamos.
* Explica siempre el porqué antes del cómo.
* No escribas código automáticamente sin justificar el diseño.
* Hazme participar en decisiones importantes.
* Divide problemas grandes en pasos pequeños.
* Señala malas prácticas cuando aparezcan.
* Prioriza simplicidad, aprendizaje y buenas prácticas profesionales.
* No avances saltando etapas.
* Antes de implementar un componente nuevo, define responsabilidades, flujo y decisiones de diseño.

==================================================
PROYECTO
========

Nombre del repositorio:

civil-budget-ai

Repositorio GitHub:

Carlosp-civil/civil-budget-ai

Sistema:

Windows

Objetivo:

Construir una plataforma que analice presupuestos de obra en Excel o CSV utilizando Python e inteligencia artificial.

Objetivo profesional:

Crear un proyecto de portafolio para Ingeniería Civil que resuelva problemas reales del sector construcción.

La aplicación debe ayudar a:

* limpiar presupuestos;
* normalizar nombres de ítems;
* detectar inconsistencias;
* analizar información de costos;
* aplicar conocimiento de ingeniería civil;
* generar dashboards;
* utilizar IA para sugerencias y aprendizaje.

==================================================
STACK ACTUAL
============

Tecnologías utilizadas:

* Python
* Git
* GitHub
* VS Code
* pandas
* openpyxl
* pytest

Tecnologías futuras:

* Streamlit
* Plotly
* IA para sugerencias y aprendizaje

==================================================
ESTRUCTURA ACTUAL
=================

civil-budget-ai/

app/

├── ingestion/
│
│   ├── **init**.py
│   ├── models.py
│   ├── file_detector.py
│   ├── file_loader.py
│   └── column_detector.py
│
├── normalization/
│
│   ├── **init**.py
│   ├── text_normalizer.py
│   ├── domain_normalizer.py
│   └── models.py
│
├── analysis/
├── ui/
└── export/

data/

├── samples/
├── outputs/
└── knowledge/
└── domain_aliases.json

tests/

├── test_file_detector.py
├── test_file_loader.py
├── test_domain_normalizer.py
├── test_column_detector.py
└── test_ingestion_models.py

==================================================
MVP DEFINIDO
============

Primera versión:

1. Usuario carga Excel o CSV.
2. Sistema analiza estructura.
3. Detecta columnas.
4. Normaliza información.
5. Consulta conocimiento existente.
6. Sugiere equivalencias.
7. Usuario valida.
8. Sistema aprende equivalencias.
9. Genera análisis básico.

Columnas objetivo:

* codigo
* descripcion
* unidad
* cantidad
* precio_unitario

==================================================
DECISIONES IMPORTANTES DE DISEÑO
================================

1. Normalización contextual.

No todos los campos deben limpiarse igual.

Reglas actuales:

codigo:

* normalización agresiva.

descripcion:

* conservar caracteres técnicos.

unidad:

* conservar caracteres técnicos.

cantidad:

* normalización agresiva.

precio_unitario:

* normalización agresiva.

Debe conservar:

f'c=21 MPa

kg/cm²

Ø4"

Debe limpiar:

Cant.

Descripción.

==================================================
COMPONENTES IMPLEMENTADOS
=========================

1. TextNormalizer

Responsabilidad:

Solo limpieza general de texto.

NO conoce Ingeniería Civil.

Permite:

normalize(
text,
preserve_special_chars=True/False
)

Conserva caracteres técnicos:

# '

/
²
³
Ø
%

==================================================
2. DomainNormalizer
===================

Responsabilidad:

* cargar conocimiento del dominio;
* crear mapa invertido;
* buscar equivalencias;
* devolver resultados con confianza.

Utiliza:

data/knowledge/domain_aliases.json

Ejemplo:

pu →

precio_unitario

Sistema de confianza:

high_confidence = 3
medium_confidence = 2
low_confidence = 1

Problema resuelto:

Dos alias diferentes pueden normalizarse igual.

Ejemplo:

p.u.

pu

Solución:

* priorización por confianza;
* agrupación por término canónico;
* conservar coincidencia de mayor confianza.

==================================================
3. FileDetector
===============

Responsabilidad:

Detectar tipo de archivo.

Soporta:

* CSV
* Excel

==================================================
4. BudgetDocument
=================

Archivo:

app/ingestion/models.py

Representa un presupuesto cargado.

Contiene:

* data: pandas.DataFrame
* filename: str
* columns: list[str]

==================================================
5. BudgetLoader
===============

Responsabilidad:

Convertir archivo externo en BudgetDocument.

Diseño:

Inyección de dependencia.

Flujo:

Archivo

↓

FileDetector

↓

BudgetLoader

↓

BudgetDocument

==================================================
6. ColumnDetector
=================

Responsabilidad actual:

Detectar columnas estándar del presupuesto.

Recibe:

list[str]

NO recibe BudgetDocument.

Razón:

Principio de responsabilidad única.

Solo analiza nombres de columnas.

Usa:

DomainNormalizer mediante inyección de dependencia.

Actualmente devuelve:

ColumnDetectionResult

==================================================
MODELOS ACTUALES
================

app/ingestion/models.py contiene:

BudgetDocument

Representa archivo cargado.

ColumnMapping

Representa decisión final:

codigo
descripcion
unidad
cantidad
precio_unitario

ColumnDetectionResult

Contiene:

mapping: ColumnMapping

warnings: list[str]

ColumnCandidate

Nuevo modelo agregado.

Representa una posible interpretación.

Campos:

column_name: str

field: str

confidence: str

source: str

Ejemplo:

ColumnCandidate(
column_name="P.U.",
field="precio_unitario",
confidence="high_confidence",
source="domain_alias"
)

==================================================
TESTS ACTUALES
==============

Último resultado:

13 passed

Incluye:

* test_file_detector.py
* test_file_loader.py
* test_domain_normalizer.py
* test_column_detector.py
* test_ingestion_models.py

==================================================
GIT
===

Últimos commits:

05f6f2b

Refactor column detector to return detection result

82a56fa

Add description column aliases

d3285f5

Add ingestion model tests and column candidate model

Último push realizado correctamente.

Estado:

main sincronizado con GitHub.

Existe un archivo local no rastreado:

docs/project_context_prompt3.md

No se ha agregado al repositorio porque parece ser documentación auxiliar de contexto.

==================================================
PUNTO EXACTO DONDE NOS QUEDAMOS
===============================

Estamos a punto de refactorizar ColumnDetector.

La decisión tomada:

Implementar una arquitectura por fases explícitas.

Nuevo flujo esperado:

columns

↓

_collect_raw_matches()

↓

list[ColumnCandidate]

↓

_resolve_conflicts()

↓

ColumnDetectionResult

↓

ColumnMapping

La primera fase debe:

* encontrar todas las posibles coincidencias;
* no tomar decisiones finales;
* devolver candidatos.

La segunda fase debe:

* resolver conflictos;
* elegir mejor coincidencia;
* generar warnings.

==================================================
PRÓXIMO PASO
============

Antes de programar:

Continuar la conversación definiendo el diseño exacto de:

_collect_raw_matches()

La decisión pendiente es:

¿Qué debe devolver?

Opción recomendada:

list[ColumnCandidate]

Razón:

Mantiene separación de responsabilidades.

La fase de recolección solo encuentra posibilidades.

La fase de resolución decide.

Continúa desde aquí:

"Vamos a diseñar _collect_raw_matches() antes de escribir código."
