# M-NMAP v2.0 – Escáner de Puertos TCP en Python

**M-NMAP v2.0** es la segunda versión de una herramienta de escaneo de puertos TCP desarrollada en Python e inspirada en funcionalidades de Nmap.

Esta versión incorpora mejoras respecto a la versión inicial, incluyendo escaneo concurrente, selección de puertos, configuración de velocidad, identificación de servicios y detección básica de versiones mediante Banner Grabbing.

El proyecto tiene fines educativos y busca fortalecer conocimientos sobre Python, redes informáticas y ciberseguridad.

## Novedades de la versión 2.0

- Incorporación de escaneo concurrente mediante ThreadPoolExecutor.
- Selección de puertos específicos y rangos personalizados.
- Escaneo de todos los puertos TCP (1–65535).
- Escaneo rápido de puertos comunes.
- Configuración de velocidad de escaneo (T1–T5).
- Identificación convencional de servicios.
- Detección básica de información mediante Banner Grabbing.
- Modo detallado para visualizar resultados.
- Resumen de puertos abiertos y tiempo de ejecución.

## Tecnologías utilizadas

- Python 3.
- Socket.
- Argparse.
- Concurrent.futures.
- Time.

No requiere instalar librerías externas.

## Requisitos

- Python 3.10 o superior.
- Windows, Linux o macOS.

## Instalación

Clona el repositorio:

```bash
git clone https://github.com/gerardogonzalez0264gg/M-NMAP.git
```

Ingresa al directorio:

```bash
cd M-NMAP
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

Escaneo rápido:

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

## Limitaciones

- Realiza escaneos mediante conexiones TCP.
- La identificación de servicios se basa en asociaciones convencionales de puertos.
- La detección de versiones es básica y depende de las respuestas de los servicios.
- No implementa detección de sistemas operativos.
- No garantiza distinguir entre puertos cerrados y filtrados.

## Consideraciones de seguridad

Esta herramienta fue desarrollada con fines educativos.

Utiliza M-NMAP únicamente contra equipos, redes o sistemas propios o sobre los cuales tengas autorización para realizar pruebas.

## Autor - GERARDO GONZÁLEZ

Proyecto personal de aprendizaje en Python y ciberseguridad.

**Versión actual: 2.0**
