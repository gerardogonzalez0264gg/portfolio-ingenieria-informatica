"""
Detección inteligente de objetos
Gerardo González

Detección inteligente de objetos:
Imagen → modelo de visión → detecciones → datos → decisión

Este archivo utiliza un modelo YOLO preentrenado. No se entrena un modelo nuevo.
"""

from pathlib import Path
import urllib.request

import matplotlib.pyplot as plt
import pandas as pd
from PIL import Image
from ultralytics import YOLO

modelo = YOLO("yolo26n.pt")

imagen = Path("imagen.jpg")

if not imagen.exists():
    print("Descargando imagen de prueba...")
    urllib.request.urlretrieve(
        "https://ultralytics.com/images/bus.jpg",
        imagen
    )

imagen_pil = Image.open(imagen)

plt.figure(figsize=(10, 7))
plt.imshow(imagen_pil)
plt.axis("off")
plt.title("Imagen de entrada")
plt.show()

resultado = modelo.predict(
    source=str(imagen),
    conf=0.25,
    verbose=False
)[0]

print(f"Cantidad de objetos detectados: {len(resultado.boxes)}")

imagen_detecciones = resultado.plot()

plt.figure(figsize=(12, 8))
plt.imshow(imagen_detecciones[:, :, ::-1])
plt.axis("off")
plt.title("Detecciones realizadas por YOLO")
plt.show()

nombres_clases = {
    "person": "persona",
    "bicycle": "bicicleta",
    "car": "auto",
    "motorcycle": "motocicleta",
    "bus": "bus",
    "truck": "camión",
    "traffic light": "semáforo",
    "stop sign": "señal de pare"
}

detecciones = []

for caja in resultado.boxes:
    clase_id = int(caja.cls[0])
    clase_modelo = resultado.names[clase_id]
    confianza = float(caja.conf[0])

    x1, y1, x2, y2 = caja.xyxy[0].tolist()

    detecciones.append({
        "objeto": nombres_clases.get(clase_modelo, clase_modelo),
        "clase_modelo": clase_modelo,
        "confianza": round(confianza, 3),
        "x1": round(x1, 2),
        "y1": round(y1, 2),
        "x2": round(x2, 2),
        "y2": round(y2, 2)
    })

datos = pd.DataFrame(detecciones)

print("\nDatos obtenidos de las detecciones:")
print(datos.to_string(index=False))

clases_detectadas = set(datos["clase_modelo"]) if not datos.empty else set()

hay_persona = "person" in clases_detectadas
hay_vehiculo = bool(
    {"bus", "car", "truck"} & clases_detectadas
)

if hay_persona and hay_vehiculo:
    decision = "ATENCIÓN"
elif hay_persona:
    decision = "INFORMACIÓN"
elif not datos.empty:
    decision = "INFORMACIÓN"
else:
    decision = "SIN DETECCIONES"

print(f"\nDecisión del sistema: {decision}")

print("\nResumen del sistema:")
print("1. Entrada: imagen")
print("2. Percepción: modelo YOLO")
print("3. Representación: objetos, confianza y coordenadas")
print("4. Decisión: lógica basada en los objetos detectados")
print(f"5. Salida: {decision}")
