# UTN - Tecnicatura Universitaria en Programación (TUP)
## Cátedra: Organización Empresarial (2026)

### Trabajo Práctico: Gestión Colaborativa, Control de Versiones y Organización Empresarial (Git, GitHub y Jira)

---

##  Visión General del Proyecto

Este proyecto consiste en el desarrollo de un sistema modular para el **Análisis de Datos Climáticos (Escenario A)**, integrado bajo el paradigma de **Aprendizaje Basado en Problemas (ABP)**. La solución no solo aborda el procesamiento estadístico de variables meteorológicas, sino que sirve como entorno de validación para la integración de herramientas de gestión empresarial (**Jira**) con sistemas de control de versiones distribuido (**Git/GitHub**) aplicados desde entornos virtuales (**Google Colab**).

*   **Hugo (P1 - Líder y Organizador):** Responsable de la gobernanza, estructura de directorios y documentación.
*   **Paco (P2 - Desarrollador Técnico):** Responsable de la lógica algorítmica de análisis y graficación.
*   **Luis (P3 - Revisor y QA):** Responsable de la auditoría de seguridad de credenciales, calidad de código y gestión de Pull Requests.

---

##  Escenario Seleccionado: Escenario A – Análisis de Datos Climáticos

El sistema procesa registros meteorológicos históricos mensuales para generar indicadores clave de rendimiento climático que faciliten la toma de decisiones agrícolas, energéticas o de planificación urbana.

### Objetivos Técnicos:
*   **Importar y procesar** datos de temperatura (mínimas, máximas, medias) y precipitaciones.
*   **Calcular indicadores:** Temperatura promedio anual, temperaturas extremas absolutas con detección de mes de ocurrencia y promedios de pluviosidad.
*   **Visualizar información:** Generación de un gráfico de doble eje que correlacione la temperatura media (línea) y las precipitaciones (barras).
*   **Garantizar reproducibilidad:** Asegurar la ejecución del script mediante el uso estricto de rutas relativas.

---

##  Descripción del Dataset Utilizado

El proyecto utiliza un dataset simulado de alta fidelidad guardado en `datos/registro_climatico.csv`, que emula series temporales de estaciones meteorológicas abiertas (Open Data).

**Estructura del archivo de datos:**
| Columna | Tipo de Dato | Descripción |
| :--- | :--- | :--- |
| `Mes` | Texto | Nombre del mes registrado (Enero a Diciembre) |
| `Temperatura_Min` | Float | Registro de temperatura mínima observada en °C |
| `Temperatura_Max` | Float | Registro de temperatura máxima observada en °C |
| `Precipitaciones` | Float | Volumen de lluvias acumulado en milímetros (mm) |
| `Temperatura_Media` | Float | Calculada dinámicamente como `(Min + Max) / 2` |

---

##  Estructura del Repositorio

Siguiendo las buenas prácticas de ingeniería de software sugeridas por la cátedra, el repositorio mantiene la siguiente jerarquía de archivos:

```text
tp-organizacion-clima/
│
├── datos/
│   └── registro_climatico.csv      # Dataset en formato CSV
│
├── scripts/
│   └── analisis_datos.py           # Código ejecutable en Python
│
├── resultados/
│   ├── grafico_temperatura.png     # Visualización de datos exportada
│   └── reporte_indicadores.txt     # Reporte de texto plano generado
│
├── .gitignore                      # Exclusión de archivos basura y temporales
└── README.md                       # Documentación general del proyecto
