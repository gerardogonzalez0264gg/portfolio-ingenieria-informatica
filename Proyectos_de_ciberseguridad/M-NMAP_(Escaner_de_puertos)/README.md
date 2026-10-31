# M-NMAP

**M-NMAP** es una herramienta de escaneo de puertos TCP desarrollada en Python e inspirada en Nmap. Este proyecto tiene como objetivo aprender y comprender conceptos de redes, conexiones TCP, identificación de servicios y reconocimiento básico de versiones.

## Características

- Escaneo de puertos TCP.
- Selección personalizada de puertos.
- Escaneo de todos los puertos TCP (1–65535).
- Escaneo rápido de puertos comunes.
- Escaneo concurrente mediante ThreadPoolExecutor.
- Modo detallado (Verbose).
- Identificación básica de servicios.
- Detección básica de versiones mediante Banner Grabbing.
- Configuración de velocidad de escaneo (T1–T5).

## Tecnologías utilizadas

- Python 3
- Socket
- Argparse
- Concurrent.futures
- Time

## Requisitos

- Python 3.10 o superior.
- No requiere instalar librerías externas.

## Instalación

Clona el repositorio:

```bash
git clone https://github.com/gerardogonzalez0264gg/M-NMAP.git
```

Accede a la carpeta del proyecto:

```bash
cd M-NMAP
```

## Uso

Ejecutar un escaneo básico de los primeros 1000 puertos TCP:

```bash
python M-NMAP.py 127.0.0.1
```

### Opciones disponibles

| Opción | Descripción |
|---|---|
| `-p` | Especificar puertos o rangos de puertos. |
| `-p-` | Escanear todos los puertos TCP (1–65535). |
| `-F` | Escanear una lista de puertos comunes. |
| `-v` | Activar el modo detallado (Verbose). |
| `-sV` | Intentar identificar servicios y versiones. |
| `-T1` a `-T5` | Configurar la velocidad del escaneo. |
| `-h` | Mostrar la ayuda del programa. |

### Ejemplos de uso

**Escanear puertos específicos:**

```bash
python M-NMAP.py 127.0.0.1 -p 22,80,443
```

**Escanear un rango de puertos:**

```bash
python M-NMAP.py 127.0.0.1 -p 1-1000
```

**Escanear todos los puertos TCP:**

```bash
python M-NMAP.py 127.0.0.1 -p-
```

**Escaneo rápido de puertos comunes:**

```bash
python M-NMAP.py 127.0.0.1 -F
```

**Activar modo detallado:**

```bash
python M-NMAP.py 127.0.0.1 -v
```

**Intentar detectar servicios y versiones:**

```bash
python M-NMAP.py 127.0.0.1 -sV
```

**Combinar diferentes opciones:**

```bash
python M-NMAP.py 127.0.0.1 -p 1-1000 -sV -v -T4
```

## Limitaciones actuales

- Actualmente realiza escaneos mediante conexiones TCP completas.
- La identificación de servicios se basa en las asignaciones convencionales de puertos.
- La detección de versiones utiliza Banner Grabbing básico y no cuenta con la capacidad de identificación avanzada de Nmap.
- La inspección de versiones HTTPS/TLS todavía no está implementada.
- No incluye detección del sistema operativo.
- No distingue de forma fiable entre puertos cerrados y filtrados.

## Aviso de seguridad

Este proyecto fue desarrollado con fines educativos y para realizar pruebas de seguridad autorizadas.

Utiliza la herramienta únicamente contra equipos, redes y sistemas propios o para los que tengas autorización explícita.

## Mejoras futuras

- Mejorar la identificación de servicios y versiones.
- Implementar inspección HTTPS/TLS.
- Incorporar detección del sistema operativo.
- Exportar resultados en formatos JSON, TXT y HTML.
- Desarrollar una interfaz gráfica.
- Mejorar la identificación de estados de los puertos.

## Autor

Desarrollado como proyecto personal de aprendizaje en ciberseguridad utilizando Python.
