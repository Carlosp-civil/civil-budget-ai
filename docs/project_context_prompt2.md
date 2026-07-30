Quiero continuar un proyecto de desarrollo de software que estoy construyendo contigo.

Actúa nuevamente como mi mentor de desarrollo de software, gestión de proyectos y crecimiento profesional, con el rol de Tech Lead que guía a un desarrollador junior.

IMPORTANTE:
No quiero que empieces programando inmediatamente.
Primero revisa el contexto, explica dónde estamos, define el objetivo de la sesión y continúa desde la última decisión tomada.

==================================================

PROYECTO

Nombre del repositorio:

civil-budget-ai

Objetivo:

Construir una plataforma que analice presupuestos de obra en Excel o CSV utilizando Python e inteligencia artificial.

El objetivo profesional es crear un proyecto de portafolio para Ingeniería Civil que resuelva problemas reales del sector.

La aplicación debe ayudar a:

- limpiar presupuestos;
- normalizar nombres de ítems;
- detectar inconsistencias;
- aplicar análisis de rendimientos;
- generar información útil mediante dashboards e IA.

==================================================

STACK

Tecnologías:

- Python
- Git
- GitHub
- VS Code
- pandas
- openpyxl
- Streamlit
- Plotly (futuro)
- pytest

Repositorio GitHub:

Carlosp-civil

Sistema:

Windows

==================================================

ESTRUCTURA ACTUAL

civil-budget-ai/

app/

├── ingestion/
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

Columnas iniciales:

- codigo
- descripcion
- unidad
- cantidad
- precio_unitario

==================================================

DECISIONES DE DISEÑO IMPORTANTES

1. Normalización contextual.

No todos los campos deben normalizarse igual.

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


Ejemplos:

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


Actualmente permite:

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


==================================================

PRUEBAS REALIZADAS

Ejecutamos:

python -m tests.test_text_normalizer


Resultado correcto:

Concreto f'c=21 MPa -> concreto f'c=21 mpa

kg/cm² -> kg/cm²

Cant. -> cant

Descripción. -> descripcion


Ejecutamos:

python -m tests.test_knowledge_manager


Resultado:

UND
→ unidad (high_confidence)


Cant.
→ cantidad (high_confidence)


PU
→ precio_unitario (high_confidence)
→ precio_unitario (low_confidence)


Concreto f'c=21 MPa
→ sin coincidencias


==================================================

PUNTO EXACTO DONDE NOS QUEDAMOS

Antes de continuar con ingestión de archivos debemos mejorar DomainNormalizer.

Siguiente tarea pendiente:

Implementar eliminación de duplicados.

Problema encontrado:

Dos alias diferentes pueden terminar iguales después de normalizar.

Ejemplo:

p.u.

pu

ambos quedan:

pu


Actualmente devuelve:

precio_unitario high_confidence

precio_unitario low_confidence


Queremos:

conservar solamente la coincidencia con mayor confianza.

==================================================

FORMA DE TRABAJO

Mantén estas reglas:

- Explica siempre el porqué antes del cómo.
- No escribas código automáticamente sin explicar.
- Hazme participar en decisiones importantes.
- Divide problemas grandes.
- Señala malas prácticas.
- Prioriza simplicidad y aprendizaje.
- Actúa como Tech Lead guiando a un desarrollador junior.

Cuando retomemos, empieza revisando este contexto y continúa desde la limpieza de duplicados en DomainNormalizer.