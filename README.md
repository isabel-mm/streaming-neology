# Neologismos en Corpus de Tweets 🐦📚

Este repositorio contiene un corpus de tweets y herramientas para procesarlo y extraer neologismos.

## Contenido del Repositorio 📂

- **Corpus de Tweets**: Una colección de tweets para ser analizados.
- **Código de Procesamiento**: Scripts para procesar y analizar el corpus.
- **`concordance_finder.py`**: Una herramienta para realizar búsquedas de concordancias y exportar los resultados en un archivo CSV.

## Funcionalidades 🚀

### 1. Procesamiento del Corpus 🧹
El repositorio contiene varias funciones para preprocesar los tweets, eliminando ruido y normalizando los datos para su análisis posterior. Puedes aplicar estos pasos de procesamiento a cualquier conjunto de datos similar de tweets.

### 2. Identificación de Neologismos 🔤
Las funciones en el repositorio permiten detectar neologismos dentro del corpus de tweets. Los resultados incluyen palabras recién acuñadas o términos de uso reciente que aún no están totalmente establecidos en el idioma.

### 3. Búsqueda de Concordancias 🔍
El script `concordance_finder.py` permite buscar concordancias de palabras o frases dentro del corpus de tweets. Puedes especificar las palabras clave y obtener el contexto en el que se usan, lo que es útil para estudiar patrones lingüísticos y la aparición de neologismos.

### 4. Exportación a CSV 📊
Los resultados de las búsquedas de concordancia se pueden exportar fácilmente a un archivo CSV para su análisis posterior en herramientas como Excel, R, o Python. Esto permite una manipulación y visualización más detallada de los datos.

## Uso 🛠️

### Requisitos ⚙️

- Python 3.x
- Librerías necesarias:
  - `pandas`
  - `nltk`
  - `re` (para expresiones regulares)
  - `csv`

Puedes instalar las librerías necesarias ejecutando:

```bash
pip install -r requirements.txt
