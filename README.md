# Data Preprocessing App

Esta es una aplicación de consola interactiva en Python que permite realizar un flujo completo de preprocesamiento de datos, visualización y exportación. Ideal para preparar datasets antes de usarlos en modelos de Machine Learning.

## Funcionalidades principales

- Carga de datos desde archivos CSV, Excel o SQLite.
- Selección de columnas de entrada y salida.
- Manejo flexible de valores faltantes.
- Transformación de variables categóricas (One-Hot o Label Encoding).
- Normalización y escalado de variables numéricas.
- Detección y manejo de valores atípicos.
- Visualización estadística y gráfica de los datos.
- Exportación de los datos preprocesados en formato CSV o Excel.

## Requisitos

- Python 3.7+
- pandas
- scikit-learn
- matplotlib
- seaborn
- openpyxl

Puedes instalar las dependencias ejecutando:

```bash
pip install -r requirements.txt


## Ejecutar pruebas

Desde la raíz del proyecto ejecutar:

python tests/test_runner.py

