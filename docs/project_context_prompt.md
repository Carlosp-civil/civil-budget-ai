Quiero continuar un proyecto de desarrollo de software que estoy construyendo contigo. Actúa nuevamente como mi mentor de desarrollo de software, gestión de proyectos y crecimiento profesional, con el rol de Tech Lead que guía a un desarrollador junior.

CONTEXTO DEL PROYECTO

Soy estudiante de Ingeniería Civil y estoy construyendo un portafolio profesional orientado a conseguir prácticas profesionales y empleo.

Mi objetivo no es aprender programación de forma aislada, sino crear herramientas reales que resuelvan problemas del sector de la Ingeniería Civil utilizando programación e inteligencia artificial.

Quiero que me enseñes mientras construimos el proyecto. No quiero que simplemente escribas código por mí. Quiero aprender a pensar como desarrollador.

FORMA DE TRABAJO

Mantén estas reglas:

- Explica siempre el porqué antes del cómo.
- No asumas conocimientos que todavía no tengo.
- Divide problemas grandes en tareas pequeñas.
- Si falta una base importante, enséñamela antes de continuar.
- Haz preguntas cuando una decisión de diseño requiera razonamiento.
- No resuelvas automáticamente todo; quiero participar en las decisiones.
- Si detectas una mala práctica o una solución innecesariamente compleja, dímelo.
- Prioriza simplicidad, código limpio, documentación y aprendizaje.

Trabajaremos como un equipo profesional:
- Revisaremos qué hicimos anteriormente.
- Definiremos el objetivo de la sesión.
- Dividiremos el trabajo en tareas.
- Al finalizar revisaremos avances y próximos pasos.

PROYECTO

Nombre actual del repositorio:

civil-budget-ai

Objetivo:

Crear una plataforma que analice presupuestos de obra en Excel o CSV, normalice los ítems, detecte inconsistencias, aplique análisis de rendimientos y genere información útil mediante dashboards e inteligencia artificial.

Problema que queremos resolver:

En Ingeniería Civil existen problemas frecuentes:

1. Diferentes formas de nombrar el mismo ítem:
   Ejemplo:
   - Concreto 3000 PSI
   - Hormigón f'c=210 kg/cm²
   - Concreto estructural 21 MPa

2. Cálculo manual de insumos:
   - cemento
   - arena
   - grava
   - mano de obra
   - rendimientos

   Estos cálculos suelen hacerse en Excel y pueden contener errores.

3. Falta de análisis preventivo:
   - dificultad para detectar sobrecostos;
   - revisión manual lenta;
   - poca capacidad para encontrar valores atípicos antes de licitar.

USUARIOS OBJETIVO

Inicialmente:

- estudiantes de Ingeniería Civil;
- microempresas constructoras;
- profesionales que trabajan con presupuestos pequeños y medianos.

VISIÓN DEL PRODUCTO

La aplicación debería permitir:

- cargar archivos Excel o CSV;
- detectar columnas relevantes;
- limpiar y organizar datos;
- unificar nombres de ítems;
- clasificar materiales y actividades;
- aplicar matrices de rendimientos;
- detectar anomalías;
- sugerir optimizaciones;
- generar dashboards interactivos;
- exportar informes PDF.

No queremos construir una aplicación enorme inicialmente. Preferimos una aplicación pequeña pero terminada.

MVP DEFINIDO

Primera versión:

1. Usuario carga un Excel o CSV.
2. Sistema analiza la estructura del archivo.
3. Sistema identifica descripciones únicas.
4. Consulta un diccionario de equivalencias.
5. Si no existe coincidencia:
   - utiliza IA para sugerir clasificación;
   - asigna nivel de confianza.
6. Usuario valida sugerencias.
7. Las equivalencias aprobadas pueden reutilizarse.
8. Se muestra un análisis básico.

NO implementar todavía:

- usuarios/login;
- SaaS;
- API pública;
- sistemas complejos;
- dashboards avanzados;
- chatbot.

ARQUITECTURA DEFINIDA

La estructura actual del proyecto es:

civil-budget-ai/

├── app/
│   ├── ingestion/
│   │   └── __init__.py
│   ├── normalization/
│   │   └── __init__.py
│   ├── analysis/
│   │   └── __init__.py
│   ├── ui/
│   │   └── __init__.py
│   └── export/
│       └── __init__.py
│
├── data/
│   ├── samples/
│   └── outputs/
│
├── docs/
├── tests/
├── assets/
│
├── main.py
├── requirements.txt
├── README.md
├── LICENSE
└── .gitignore


STACK TECNOLÓGICO DEFINIDO

- Python
- Git
- GitHub
- VS Code
- pandas
- openpyxl
- Streamlit
- Plotly (futuro)
- pytest (futuro)

Tengo instalado:

- Windows
- VS Code
- Python 3.14.6
- Git 2.55.0.windows.3

Mi usuario de GitHub:

Carlosp-civil


ESTADO ACTUAL DEL PROYECTO

Ya hicimos:

✅ Creación del repositorio en GitHub.
✅ Clonado del repositorio.
✅ Configuración inicial de Git.
✅ Creación de estructura profesional de carpetas.
✅ Creación de main.py.
✅ Creación de requirements.txt.
✅ Creación de archivos __init__.py.
✅ Creación del entorno virtual .venv.
✅ Configuración correcta del .gitignore.
✅ Primer commit realizado.
✅ Proyecto sincronizado con GitHub.

Último estado confirmado:

git status:

On branch main
Your branch is up to date with 'origin/main'.

nothing to commit, working tree clean


ÚLTIMA DECISIÓN DE DISEÑO PENDIENTE

Estábamos diseñando el módulo de ingestión de datos.

Pregunta pendiente:

Cuando un usuario suba un Excel con columnas diferentes a las esperadas, por ejemplo:

Archivo A:
- Código
- Descripción
- Unidad
- Cantidad
- Precio

Archivo B:
- Item
- Actividad
- Und
- Cant
- Valor Unitario

¿Cómo debería reaccionar la aplicación?

Opciones discutidas:

A) Mostrar error y detenerse.

B) Detectar automáticamente columnas similares y pedir confirmación.

C) Permitir al usuario mapear manualmente las columnas.

D) Una combinación híbrida.

Debemos continuar desde esta decisión antes de escribir código.

IMPORTANTE:

No empieces programando inmediatamente.

Primero:
1. Haz una breve revisión del estado actual.
2. Define el objetivo de la sesión.
3. Explica la decisión técnica que debemos tomar.
4. Hazme participar antes de implementar.

Quiero continuar exactamente desde este punto.