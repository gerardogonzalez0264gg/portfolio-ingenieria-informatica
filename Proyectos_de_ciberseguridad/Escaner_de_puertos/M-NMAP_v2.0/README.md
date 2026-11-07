
# M-NMAP — Escáner de Puertos TCP en Python

## Descripción

M-NMAP es una herramienta de escaneo de puertos TCP desarrollada en Python e inspirada en Nmap. Permite analizar hosts de una red, identificar puertos abiertos, reconocer servicios y obtener información mediante técnicas de Banner Grabbing.

## Objetivo

Desarrollar una herramienta de escaneo de puertos TCP que permita analizar hosts, identificar servicios y obtener información básica de los dispositivos de una red, aplicando conocimientos de programación Python, protocolos de red y ciberseguridad.

## Características principales

- Escaneo de puertos TCP.
- Selección de puertos específicos.
- Escaneo de rangos personalizados.
- Escaneo completo de puertos TCP (1–65535).
- Escaneo rápido de puertos comunes.
- Ejecución concurrente mediante `ThreadPoolExecutor`.
- Configuración de velocidad de escaneo (T1–T5).
- Identificación convencional de servicios.
- Detección básica de información mediante Banner Grabbing.
- Soporte básico para conexiones HTTPS/TLS.
- Visualización del progreso del escaneo.
- Modo detallado de ejecución.
- Exportación de resultados en formatos TXT y JSON.
- Resumen de puertos abiertos y tiempo de ejecución.

## Tecnologías utilizadas

- Python 3.10 o superior.
- Socket.
- Argparse.
- Concurrent.futures.
- JSON.
- SSL.
- Datetime.

**Dependencias:** No requiere instalar librerías externas.

## Requisitos

- Python 3.10 o superior.
- Windows, Linux o macOS.

## Instalación

Clonar el repositorio:

```bash
git clone https://github.com/gerardogonzalez0264gg/portfolio-ingenieria-informatica.git
```

Ingresar al directorio del proyecto:

```bash
cd portfolio-ingenieria-informatica/Proyectos_de_ciberseguridad/Escaner_de_puertos/M-NMAP_v2.0
```

## Uso

### Escaneo básico

```bash
python M-NMAP.py 127.0.0.1
```

### Escaneo de puertos específicos

```bash
python M-NMAP.py 127.0.0.1 -p 22,80,443
```

### Escaneo de un rango de puertos

```bash
python M-NMAP.py 127.0.0.1 -p 1-1000
```

### Escaneo de todos los puertos TCP

```bash
python M-NMAP.py 127.0.0.1 -p-
```

### Escaneo rápido de puertos comunes

```bash
python M-NMAP.py 127.0.0.1 -F
```

### Detección básica de versiones

```bash
python M-NMAP.py 127.0.0.1 -sV
```

### Modo detallado

```bash
python M-NMAP.py 127.0.0.1 -v
```

### Configuración de velocidad

```bash
python M-NMAP.py 127.0.0.1 -T4
```

### Exportar resultados en TXT

```bash
python M-NMAP.py 127.0.0.1 -o informe.txt
```

### Exportar resultados en JSON

```bash
python M-NMAP.py 127.0.0.1 -o informe.json --format json
```

## Niveles de velocidad

La herramienta dispone de cinco niveles de velocidad:

| Nivel | Descripción |
|---|---|
| T1 | Muy lento |
| T2 | Lento |
| T3 | Normal |
| T4 | Rápido |
| T5 | Muy rápido |

Los niveles superiores permiten realizar escaneos más rápidos, aunque pueden aumentar la posibilidad de perder respuestas dependiendo de las condiciones de la red.

## Limitaciones

- Realiza únicamente escaneos TCP.
- La identificación de servicios se basa en asociaciones convencionales de puertos.
- Banner Grabbing depende de las respuestas entregadas por los servicios.
- El soporte HTTPS/TLS no garantiza identificar el software o su versión.
- No implementa detección de sistemas operativos.
- No garantiza distinguir entre puertos cerrados y filtrados en todos los escenarios.

## Consideraciones de seguridad

Esta herramienta fue desarrollada con fines educativos y de pruebas de seguridad autorizadas.

Utiliza M-NMAP únicamente en equipos, redes o sistemas propios o sobre los cuales tengas autorización para realizar escaneos.

## Autor

**Gerardo González**

GitHub: https://github.com/gerardogonzalez0264gg
