# M-NMAP — TCP Port Scanner

M-NMAP is a TCP port scanning tool developed in Python, inspired by Nmap. It allows users to scan network hosts, identify open ports, perform basic service detection, and retrieve service information through Banner Grabbing.

This project was developed for educational purposes to strengthen knowledge of Python programming, computer networking, and cybersecurity.

## Features

- TCP port scanning.
- Custom port selection.
- Custom port range scanning.
- Full TCP port scanning (1–65535).
- Fast scanning of common ports.
- Concurrent scanning using `ThreadPoolExecutor`.
- Configurable scanning speed (T1–T5).
- Basic service identification.
- Banner Grabbing.
- Basic HTTPS/TLS support.
- Real-time scanning progress.
- Detailed output mode.
- Results export in TXT and JSON formats.
- Summary of open ports and scan execution time.

## Technologies

- Python 3.10+
- Socket
- Argparse
- Concurrent.futures
- JSON
- SSL
- Datetime

**Dependencies:** No external libraries required.

## Requirements

- Python 3.10 or higher.
- Windows, Linux, or macOS.

## Installation

Clone the repository:

```bash
git clone https://github.com/gerardogonzalez0264gg/portfolio-ingenieria-informatica.git
```

Navigate to the project directory:

```bash
cd portfolio-ingenieria-informatica/Proyectos_de_ciberseguridad/Escaner_de_puertos/M-NMAP_v2.0
```

## Usage

### Basic scan

```bash
python M-NMAP.py 127.0.0.1
```

### Scan specific ports

```bash
python M-NMAP.py 127.0.0.1 -p 22,80,443
```

### Scan a port range

```bash
python M-NMAP.py 127.0.0.1 -p 1-1000
```

### Scan all TCP ports

```bash
python M-NMAP.py 127.0.0.1 -p-
```

### Fast scan

```bash
python M-NMAP.py 127.0.0.1 -F
```

### Service detection

```bash
python M-NMAP.py 127.0.0.1 -sV
```

### Verbose mode

```bash
python M-NMAP.py 127.0.0.1 -v
```

### Configure scanning speed

```bash
python M-NMAP.py 127.0.0.1 -T4
```

### Export results to TXT

```bash
python M-NMAP.py 127.0.0.1 -o report.txt
```

### Export results to JSON

```bash
python M-NMAP.py 127.0.0.1 -o report.json --format json
```

## Scanning Speed

M-NMAP provides five scanning speed levels:

| Level | Description |
|---|---|
| T1 | Very slow |
| T2 | Slow |
| T3 | Normal |
| T4 | Fast |
| T5 | Very fast |

Higher speeds may increase the possibility of missed responses depending on network conditions.

## Limitations

- Supports TCP scanning only.
- Service identification relies on conventional port associations.
- Banner Grabbing depends on the responses provided by services.
- HTTPS/TLS support does not guarantee software or version identification.
- Does not implement operating system detection.
- Cannot reliably distinguish filtered ports from closed ports in every situation.

## Security Notice

This tool was developed for educational and authorized security testing purposes.

Only scan systems, networks, and devices that you own or have explicit permission to test.

## Author

**Gerardo González**

GitHub: [@gerardogonzalez0264gg](https://github.com/gerardogonzalez0264gg)
