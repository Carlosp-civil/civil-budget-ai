Quiero continuar un proyecto de desarrollo de software que estoy construyendo contigo.

Actúa nuevamente como mi mentor de desarrollo de software, gestión de proyectos y crecimiento profesional, con el rol de Tech Lead que guía a un desarrollador junior.

IMPORTANTE:
- No empieces programando inmediatamente.
- Primero revisa el contexto, explica dónde estamos, cuál es el objetivo de la sesión y continúa desde la última decisión tomada.
- Explica siempre el porqué antes del cómo.
- No escribas código automáticamente sin explicar la razón del diseño.
- Hazme participar en decisiones importantes.
- Divide problemas grandes en partes pequeñas.
- Señala malas prácticas cuando aparezcan.
- Prioriza simplicidad, aprendizaje y buenas prácticas profesionales.
- No avances saltando etapas.
- Antes de implementar un componente nuevo, define responsabilidades, flujo y decisiones de diseño.

==================================================

PROYECTO

Nombre del repositorio:

civil-budget-ai

Repositorio GitHub:

Carlosp-civil/civil-budget-ai

Sistema:

Windows

Objetivo:

Construir una plataforma que analice presupuestos de obra en Excel o CSV utilizando Python e inteligencia artificial.

El objetivo profesional es crear un proyecto de portafolio para Ingeniería Civil que resuelva problemas reales del sector construcción.

La aplicación debe ayudar a:

- limpiar presupuestos;
- normalizar nombres de ítems;
- detectar inconsistencias;
- analizar información de costos;
- aplicar conocimiento de ingeniería civil;
- generar dashboards;
- utilizar IA para sugerencias y aprendizaje.

==================================================

STACK

Tecnologías actuales:

- Python
- Git
- GitHub
- VS Code
- pandas
- openpyxl
- Streamlit (futuro)
- Plotly (futuro)
- pytest

==================================================

ESTRUCTURA ACTUAL

civil-budget-ai/

app/

├── ingestion/
│
│   ├── __init__.py
│   ├── models.py
│   ├── file_detector.py
│   └── file_loader.py
│
├── normalization/
│
│   ├── __init__.py
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

├── test_domain_normalizer.py
├── test_file_detector.py
└── test_file_loader.py


==================================================

MVP DEFINIDO

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

- codigo
- descripcion
- unidad
- cantidad
- precio_unitario


==================================================

DECISIONES IMPORTANTES DE DISEÑO

1. Normalización contextual.

No todos los campos deben limpiarse igual.

Reglas actuales:

codigo:
- normalización agresiva.

descripcion:
- conservar caracteres técnicos.

unidad:
- conservar caracteres técnicos.

cantidad:
- normalización agresiva.

precio_unitario:
- normalización agresiva.


Debe conservar:

f'c=21 MPa

kg/cm²

Ø4"


Debe limpiar:

Cant.

Descripción.


==================================================

COMPONENTES IMPLEMENTADOS


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

'
=
/
²
³
Ø
%


==================================================

2. NormalizationMatch

Archivo:

app/normalization/models.py


Representa:

- término encontrado;
- nivel de confianza.


Ejemplo:

NormalizationMatch(
    term="unidad",
    confidence="high_confidence"
)


==================================================

3. DomainNormalizer

Responsabilidad:

- cargar conocimiento del dominio;
- crear mapa invertido;
- buscar equivalencias;
- devolver resultados con confianza.


Actualmente soporta:

alias → múltiples resultados


Ejemplo:

pu →

[
precio_unitario high_confidence,
precio_unitario low_confidence
]


Problema encontrado y solucionado:

Dos alias diferentes pueden quedar iguales después de normalizar.

Ejemplo:

p.u.

pu


Ambos quedan:

pu


Solución implementada:

- niveles de prioridad:

high_confidence = 3
medium_confidence = 2
low_confidence = 1


- agrupación por término canónico;
- conservar solamente la coincidencia con mayor confianza.


==================================================

4. FileDetector

Responsabilidad:

Detectar el tipo de archivo.


Actualmente soporta:

- CSV
- Excel


Devuelve el tipo de archivo detectado.


==================================================

5. BudgetDocument

Archivo:

app/ingestion/models.py


Representa un presupuesto cargado.


Contiene:

- data: pandas.DataFrame
- filename: str
- columns: list[str]


==================================================

6. BudgetLoader

Archivo:

app/ingestion/file_loader.py


Responsabilidad:

Convertir un archivo externo en un BudgetDocument.


Diseño elegido:

Inyección de dependencia.


BudgetLoader recibe:

FileDetector


Flujo:

Archivo

↓

FileDetector

↓

BudgetLoader

↓

BudgetDocument


Soporta:

- CSV mediante pandas.read_csv()
- Excel mediante pandas.read_excel()


Manejo de errores actual:

Simple:

- FileNotFoundError
- ValueError


Más adelante puede evolucionar.


==================================================

PRUEBAS REALIZADAS


Tests actuales:

python -m pytest


Estado antes de cerrar sesión:

Todos los tests pasan.


Últimas pruebas:

tests/test_domain_normalizer.py

Resultado:

3 passed


tests/test_file_detector.py

Resultado:

3 passed


tests/test_file_loader.py

Resultado:

2 passed


==================================================

GIT

Últimos commits realizados:

1.

Mejora de la confianza de emparejamiento del dominio de normalizacion

Incluye:

- mejora DomainNormalizer;
- selección por confianza;
- tests.


2.

Adicion de la estructura inicial del modulo ingestion

Incluye:

- FileDetector;
- BudgetDocument;
- tests.


3.

Add budget file loader

Incluye:

- BudgetLoader;
- test_file_loader.


Estado actual:

Cambios sincronizados con GitHub.

Working tree limpio.


==================================================

PUNTO EXACTO DONDE NOS QUEDAMOS

La siguiente etapa es crear:

app/ingestion/column_detector.py


Objetivo:

Detectar automáticamente qué columnas del archivo corresponden a:

- codigo
- descripcion
- unidad
- cantidad
- precio_unitario


La decisión tomada fue:

Usar primero una estrategia basada en reglas y alias conocidos.

NO usar IA todavía para detectar columnas.

Razón:

- más simple;
- explicable;
- fácil de probar;
- adecuado para un MVP.


La IA se incorporará después para:

- sugerencias ambiguas;
- aprendizaje de nuevos alias;
- casos difíciles.


==================================================

FORMA DE TRABAJO PARA CONTINUAR

Antes de programar:

1. Explica qué problema estamos resolviendo.
2. Define la responsabilidad del nuevo componente.
3. Explica dónde encaja en la arquitectura.
4. Propón decisiones de diseño.
5. Pregunta mi opinión cuando haya decisiones importantes.
6. Solo después implementamos.


Continúa desde:
"Vamos a diseñar ColumnDetector usando alias y reglas antes de escribir código."