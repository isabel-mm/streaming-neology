# Neologismos en Corpus de Tweets 🐦📚

Este repositorio contiene las herramientas para extraer neologismos a partir de un corpus de tweets. Este repositorio incluye los materiales utilizados para el trabajo **Moyano Moreno, I. (2026). Extracción de neologismos en Twitter/X: El léxico emergente de la comunidad hispanohablante de streaming.**

## Contenido del Repositorio 📂

- **code**: Scripts para procesar y analizar el corpus.
- **neologismos_validados**: Tabla completa con los neologismos validados e informaciones relevantes.

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
