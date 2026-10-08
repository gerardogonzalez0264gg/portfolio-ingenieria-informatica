# ARI Flow — Automatización de correos con Inteligencia Artificial

## Descripción

ARI Flow es un proyecto de automatización desarrollado en Make que utiliza inteligencia artificial para clasificar correos electrónicos y facilitar su gestión, reduciendo tareas manuales y mejorando la organización de las solicitudes recibidas.

## Objetivos

* Automatizar la clasificación de correos electrónicos.
* Diferenciar solicitudes según su contenido.
* Enviar respuestas automáticas de recepción.
* Derivar correos que requieren atención humana.
* Registrar las solicitudes clasificadas en una hoja de cálculo.

## Tecnologías utilizadas

* **Make:** creación y ejecución de flujos de automatización.
* **Gmail:** recepción, organización y envío de correos electrónicos.
* **Google Gemini AI:** clasificación de los mensajes mediante inteligencia artificial.
* **Google Drive:** acceso a archivos utilizados en el flujo.
* **Google Sheets:** registro de los correos clasificados.

## Funcionamiento

1. Gmail recibe un correo electrónico.
2. Gemini AI analiza el asunto y el contenido disponible.
3. El flujo clasifica el mensaje como `SI` o `NO`.
4. Según la clasificación, el escenario ejecuta una ruta diferente:

   * **SI:** genera una respuesta, envía el correo y registra la información en Google Sheets.
   * **NO:** deriva el mensaje a la etiqueta `Help Desk Human` y contempla el envío de una respuesta automática de recepción.

## Aprendizajes

* Diseño de flujos de automatización con Make.
* Integración de servicios de Google.
* Uso de inteligencia artificial para clasificar texto.
* Automatización de respuestas y organización de correos.
* Integración de herramientas para registrar información.

## Estado del proyecto

**En desarrollo.**

El flujo principal está configurado. Se encuentran pendientes las pruebas finales de clasificación, envío automático y gestión del estado de lectura de los mensajes.

## Estructura del proyecto

```text
ARI_Flow/
├── README.md
└── blueprint/
    └── ARI_Flow.blueprint.json
```

El archivo `blueprint` contiene la exportación del escenario de Make, si se incluye en el repositorio.

## Autor

Proyecto personal de aprendizaje y práctica en automatización, inteligencia artificial e integración de servicios.
