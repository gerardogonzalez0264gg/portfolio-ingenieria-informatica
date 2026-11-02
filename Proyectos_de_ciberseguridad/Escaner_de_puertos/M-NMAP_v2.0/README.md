# M-NMAP v2.0 – Escáner de Puertos TCP en Python

**M-NMAP v2.0** es una herramienta de escaneo de puertos TCP desarrollada en Python e inspirada en funcionalidades de Nmap.

Esta segunda versión incorpora mejoras en el escaneo concurrente, selección de puertos, identificación de servicios, detección básica de versiones y generación de informes.

Proyecto desarrollado con fines educativos para fortalecer conocimientos sobre Python, redes informáticas y ciberseguridad.

## Características principales

- Escaneo de puertos TCP.
- Selección de puertos específicos y rangos personalizados.
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

Clona el repositorio principal:

```bash
git clone https://github.com/gerardogonzalez0264gg/portfolio-ingenieria-informatica.git
```

Ingresa al directorio del proyecto:

```bash
cd portfolio-ingenieria-informatica/Proyectos_de_ciberseguridad/Escaner_de_puertos/M-NMAP_v2.0
```

## Uso

Escaneo básico:

```bash
python M-NMAP.py 127.0.0.1
```

Escaneo de puertos específicos:

```bash
python M-NMAP.py 127.0.0.1 -p 22,80,443
```

Escaneo de un rango de puertos:

```bash
python M-NMAP.py 127.0.0.1 -p 1-1000
```

Escaneo de todos los puertos TCP:

```bash
python M-NMAP.py 127.0.0.1 -p-
```

Escaneo rápido de puertos comunes:

```bash
python M-NMAP.py 127.0.0.1 -F
```

Detección básica de versiones:

```bash
python M-NMAP.py 127.0.0.1 -sV
```

Modo detallado:

```bash
python M-NMAP.py 127.0.0.1 -v
```

Configuración de velocidad:

```bash
python M-NMAP.py 127.0.0.1 -T4
```

Exportar resultados en TXT:

```bash
python M-NMAP.py 127.0.0.1 -o informe.txt
```

Exportar resultados en JSON:

```bash
python M-NMAP.py 127.0.0.1 -o informe.json --format json
```

## Limitaciones

- Realiza escaneos mediante conexiones TCP.
- La identificación de servicios se basa en asociaciones convencionales de puertos.
- La detección de versiones es básica y depende de las respuestas de los servicios.
- La detección HTTPS/TLS no garantiza identificar el software o su versión.
- No implementa detección de sistemas operativos.
- No garantiza distinguir entre puertos cerrados y filtrados.

## Consideraciones de seguridad

Esta herramienta fue desarrollada con fines educativos.

Utiliza M-NMAP únicamente contra equipos, redes o sistemas propios o sobre los cuales tengas autorización para realizar pruebas.

## Ubicación en GitHub

Repositorio: [portfolio-ingenieria-informatica](https://github.com/gerardogonzalez0264gg/portfolio-ingenieria-informatica)

Ruta del proyecto:

`Proyectos_de_ciberseguridad/Escaner_de_puertos/M-NMAP_v2.0/`

## Autor - GERARDO GONZÁLEZ

Proyecto personal de aprendizaje en Python y ciberseguridad.

**Versión: 2.0**
