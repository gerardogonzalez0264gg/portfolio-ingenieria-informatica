# M-NMAP — Escáner de Puertos TCP en Python

M-NMAP es una herramienta de escaneo de puertos TCP desarrollada en Python e inspirada en funcionalidades de Nmap.

Permite analizar puertos de un host, identificar servicios, obtener información básica mediante Banner Grabbing y generar informes con los resultados del escaneo.

Proyecto desarrollado con fines educativos para fortalecer conocimientos sobre Python, redes informáticas y ciberseguridad.

## Características principales

- Escaneo de puertos TCP.
- Selección de puertos específicos.
- Escaneo de rangos personalizados.
- Escaneo completo de puertos TCP (1–65535).
- Escaneo rápido de puertos comunes.
- Ejecución concurrente mediante ThreadPoolExecutor.
- Configuración de velocidad de escaneo (T1–T5).
- Identificación convencional de servicios.
- Detección básica de información mediante Banner Grabbing.
- Soporte básico para conexiones HTTPS/TLS.
- Visualización del progreso del escaneo.
- Exportación de resultados en formatos TXT y JSON.
- Resumen de puertos abiertos y tiempo de ejecución.

## Tecnologías utilizadas

- Python 3.
- Socket.
- Argparse.
- Concurrent.futures.
- JSON.
- SSL.
- Datetime.

No requiere instalar librerías externas.

## Requisitos

- Python 3.10 o superior.
- Windows, Linux o macOS.

## Instalación

Clona el repositorio:

```bash
git clone https://github.com/gerardogonzalez0264gg/portfolio-ingenieria-informatica.git
