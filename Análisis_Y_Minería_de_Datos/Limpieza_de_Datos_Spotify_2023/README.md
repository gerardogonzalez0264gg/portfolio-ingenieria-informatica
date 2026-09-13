# Limpieza de Datos: Spotify 2023

## 📌 Descripción del Proyecto
Este proyecto aborda la adaptación e implementación de un pipeline de limpieza y preprocesamiento de datos (*Data Preparation*) aplicado al dataset de las canciones más escuchadas en **Spotify 2023**. El objetivo principal es transformar datos crudos (*raw data*) e incompletos en un conjunto de datos estandarizado, limpio y optimizado para análisis estadísticos o modelos predictivos.

---

## 🛠️ Flujo de Trabajo (Pipeline)
1. **Carga y Análisis Exploratorio (EDA):** Carga del dataset en Pandas e inspección de variables con `head()`, `info()` y `describe()`.
2. **Limpieza de Datos:** Identificación de nulos e imputación estratégica (mediana para numéricas y moda para categóricas).
3. **Tratamiento de Outliers:** Detección de valores atípicos en la variable `streams` mediante el método del Rango Intercuartílico (IQR) y su ajuste correspondiente.
4. **Codificación Categórica:** Aplicación de *One-Hot Encoding* para la variable `key` y *Label Encoding* para `mode`.
5. **Exportación:** Generación del dataset final `spotify_limpio.csv`.

---

## 🛠️ Tecnologías Utilizadas
* **Lenguaje:** Python 3.x
* **Entorno:** Google Colab / Jupyter Notebook
* **Librerías principales:** Pandas, NumPy, Matplotlib, Seaborn
