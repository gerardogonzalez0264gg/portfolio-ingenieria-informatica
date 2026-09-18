# Detector YOLO

Sistema de detección inteligente de objetos desarrollado en Python utilizando un modelo YOLO preentrenado.

## 🎯 Objetivo

El objetivo de este proyecto es implementar un sistema capaz de analizar una imagen, detectar objetos mediante inteligencia artificial y utilizar los resultados obtenidos para tomar una decisión.

El flujo principal del sistema es:

**Imagen → Modelo YOLO → Detecciones → Datos → Decisión**

## 🔍 ¿Qué hace el proyecto?

El sistema:

1. Recibe una imagen.
2. Utiliza un modelo YOLO preentrenado para analizarla.
3. Detecta los objetos presentes en la imagen.
4. Asigna un nivel de confianza a cada detección.
5. Descarta las detecciones que estén por debajo del 25% de confianza.
6. Obtiene información de los objetos detectados:
   - Tipo de objeto.
   - Nivel de confianza.
   - Coordenadas de la detección.
7. Muestra los objetos detectados.
8. Toma una decisión según los objetos encontrados.

## 🤖 Modelo utilizado

El proyecto utiliza un modelo YOLO preentrenado mediante el archivo:

`yolo26n.pt`

No se entrena un modelo nuevo. Se utiliza el modelo preentrenado para realizar la detección de objetos en las imágenes.

## 🛠️ Tecnologías utilizadas

- Python
- YOLO
- Ultralytics
- Pandas
- Matplotlib
- PIL (Python Imaging Library)

## 📁 Estructura del proyecto

    Detector_YOLO/
    │
    ├── Detector_YOLO.py
    ├── imagen.jpg
    ├── yolo26n.pt
    └── README.md

## ⚙️ Instalación

Instala las dependencias necesarias ejecutando:

    pip install ultralytics==8.4.104
    pip install pandas matplotlib pillow

## ▶️ Uso

Ejecuta el programa con:

    python Detector_YOLO.py

El programa analizará la imagen `imagen.jpg` y mostrará las detecciones realizadas por el modelo YOLO.

## 🖼️ Utilizar una imagen propia

El proyecto actualmente está preparado para trabajar con una sola imagen de entrada, debido a las limitaciones de la implementación actual.

Para utilizar una imagen propia:

1. Reemplaza la imagen incluida en el proyecto.
2. Coloca tu nueva imagen dentro de la carpeta del proyecto.
3. Cambia el nombre de tu imagen a:

`imagen.jpg`

4. Ejecuta nuevamente el programa:

    python Detector_YOLO.py

El modelo analizará tu nueva imagen.

> **Importante:** actualmente el código permite analizar una sola imagen a la vez.

## 📊 Nivel de confianza

El sistema utiliza un umbral de confianza del **25%**:

    conf=0.25

Las detecciones con una confianza inferior al 25% son descartadas.

Las detecciones que superan este umbral continúan siendo procesadas por el sistema.

## 🧠 Lógica de decisión

Después de detectar los objetos, el sistema utiliza una lógica para tomar una decisión:

- Si detecta una persona y un vehículo → `ATENCIÓN`
- Si detecta una persona → `INFORMACIÓN`
- Si detecta otros objetos → `INFORMACIÓN`
- Si no detecta objetos → `SIN DETECCIONES`

## 📌 Funcionamiento

    Imagen
       ↓
    Modelo YOLO
       ↓
    Detección de objetos
       ↓
    Evaluación de confianza ≥ 25%
       ↓
    Objetos + confianza + coordenadas
       ↓
    Lógica de decisión
       ↓
    Resultado final

## 📚 Aprendizaje

Este proyecto permite comprender cómo integrar un modelo de inteligencia artificial con Python para construir un sistema que:

- Percibe información mediante una imagen.
- Utiliza un modelo de visión artificial.
- Convierte las detecciones en datos.
- Aplica lógica de software para generar una decisión.

## 👨‍💻 Autor

**Gerardo González**

Proyecto realizado con fines académicos y de aprendizaje en inteligencia artificial y detección de objetos.