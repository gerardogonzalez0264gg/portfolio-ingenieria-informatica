# M-NMAP

**M-NMAP** is a TCP port scanner developed in Python, inspired by Nmap. This project was created for educational purposes to understand network scanning, TCP connections, service identification and basic banner grabbing.

## Features

- TCP port scanning.
- Custom port selection.
- Full TCP port scanning (1–65535).
- Fast scanning of common ports.
- Concurrent scanning using ThreadPoolExecutor.
- Verbose mode for additional scan information.
- Basic service identification.
- Basic banner grabbing and version detection attempts.
- Adjustable scanning speed (T1–T5).

## Technologies

- Python 3
- Socket
- Argparse
- Concurrent.futures
- Time

## Requirements

- Python 3.10 or later.
- No external Python packages required.

## Installation

Clone the repository:

```bash
git clone https://github.com/gerardogonzalez0264gg/M-NMAP.git
```

Enter the project directory:

```bash
cd M-NMAP
```

## Usage

Run a basic scan of the first 1,000 TCP ports:

```bash
python M-NMAP.py 127.0.0.1
```

### Available options

| Option | Description |
|---|---|
| `-p` | Specify ports or port ranges. |
| `-p-` | Scan all TCP ports (1–65535). |
| `-F` | Scan predefined common ports. |
| `-v` | Enable verbose output. |
| `-sV` | Attempt service and version detection. |
| `-T1` to `-T5` | Adjust scanning speed. |
| `-h` | Display help information. |

### Examples

Scan specific ports:

```bash
python M-NMAP.py 127.0.0.1 -p 22,80,443
```

Scan a port range:

```bash
python M-NMAP.py 127.0.0.1 -p 1-1000
```

Scan all TCP ports:

```bash
python M-NMAP.py 127.0.0.1 -p-
```

Scan common ports:

```bash
python M-NMAP.py 127.0.0.1 -F
```

Enable verbose mode:

```bash
python M-NMAP.py 127.0.0.1 -v
```

Attempt service and version detection:

```bash
python M-NMAP.py 127.0.0.1 -sV
```

Combine multiple options:

```bash
python M-NMAP.py 127.0.0.1 -p 1-1000 -sV -v -T4
```

## Important limitations

- M-NMAP currently performs TCP connect scanning.
- Service identification uses conventional port assignments.
- Version detection uses basic banner grabbing and is not as comprehensive as Nmap's service fingerprinting.
- HTTPS/TLS version detection is not implemented yet.
- The scanner does not currently perform operating system detection.
- Unsuccessful connections are not reliably classified as closed or filtered.

## Disclaimer

This project was developed for educational purposes and authorized security testing.

Only scan computers, networks and systems that you own or have explicit permission to test.

## Future improvements

- Improved service and version detection.
- HTTPS/TLS inspection.
- Operating system fingerprinting.
- Export results to JSON, TXT and HTML.
- Graphical user interface.
- Improved port state detection.

## Author

Developed as a personal cybersecurity learning project using Python.