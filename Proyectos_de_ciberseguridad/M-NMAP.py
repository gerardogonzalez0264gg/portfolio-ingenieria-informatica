
import socket
import argparse
import concurrent.futures
import time

# Puertos comunes para escaneos rapidos
COMMON_PORTS = [
    21, 22, 23, 25, 53, 80, 110, 135, 139,
    143, 443, 445, 993, 995, 3306, 3389,
    5432, 5900, 8080, 8443
]

# Niveles de velocidad
TIMING_LEVELS = {
    1: {"workers": 5, "timeout": 2.0},
    2: {"workers": 15, "timeout": 1.5},
    3: {"workers": 50, "timeout": 1.0},
    4: {"workers": 100, "timeout": 0.5},
    5: {"workers": 200, "timeout": 0.3}
}


def get_ports(args):
    """Determina los puertos que se van a analizar."""

    if args.all_ports:
        return range(1, 65536)

    if args.ports:
        selected_ports = set()

        for item in args.ports.split(","):
            if "-" in item:
                first, last = map(int, item.split("-"))

                if first < 1 or last > 65535 or first > last:
                    raise ValueError("Rango de puertos invalido.")

                selected_ports.update(range(first, last + 1))

            else:
                port = int(item)

                if port < 1 or port > 65535:
                    raise ValueError("Puerto invalido.")

                selected_ports.add(port)

        return sorted(selected_ports)

    if args.fast:
        return COMMON_PORTS

    return range(1, 1001)


def identify_service(port):
    """Identifica el nombre habitual del servicio."""

    try:
        return socket.getservbyport(port, "tcp")
    except OSError:
        return "unknown"


def detect_version(target, port, timeout):
    """Intenta obtener informacion del servicio."""

    try:
        with socket.create_connection(
            (target, port), timeout=timeout
        ) as client:

            client.settimeout(timeout)

            # Solicitud HTTP para obtener informacion del servidor
            if port in (80, 8080, 8000):
                request = (
                    f"HEAD / HTTP/1.0\r\n"
                    f"Host: {target}\r\n\r\n"
                )
                client.sendall(request.encode())

            # HTTPS necesita una conexion TLS
            elif port in (443, 8443):
                return "Version no identificada (TLS)"

            # Leer respuesta del servicio
            banner = client.recv(1024)

            if banner:
                return banner.decode(
                    "utf-8", errors="replace"
                ).strip().replace("\r", " ").replace("\n", " ")[:100]

    except (OSError, TimeoutError):
        pass

    return "Version no identificada"


def scan_port(target, port, timeout, version_detection):
    """Comprueba si un puerto TCP esta abierto."""

    try:
        with socket.socket(
            socket.AF_INET, socket.SOCK_STREAM
        ) as client:

            client.settimeout(timeout)

            result = client.connect_ex((target, port))

            if result == 0:
                service = identify_service(port)
                version = ""

                if version_detection:
                    version = detect_version(
                        target, port, timeout
                    )

                return {
                    "port": port,
                    "state": "open",
                    "service": service,
                    "version": version
                }

    except OSError:
        pass

    return None


def main():
    parser = argparse.ArgumentParser(
        description="M-NMAP - Escaner de puertos TCP"
    )

    parser.add_argument(
        "target",
        help="Direccion IP o nombre del objetivo"
    )

    port_group = parser.add_mutually_exclusive_group()

    port_group.add_argument(
        "-p",
        "--ports",
        help="Puertos especificos. Ejemplo: 22,80,1-100"
    )

    port_group.add_argument(
        "-p-",
        "--all-ports",
        action="store_true",
        help="Analizar todos los puertos TCP"
    )

    parser.add_argument(
        "-F",
        "--fast",
        action="store_true",
        help="Analizar puertos comunes"
    )

    parser.add_argument(
        "-v",
        "--verbose",
        action="store_true",
        help="Mostrar informacion detallada"
    )

    parser.add_argument(
        "-sV",
        dest="version_detection",
        action="store_true",
        help="Intentar identificar servicios y versiones"
    )

    parser.add_argument(
        "-T",
        type=int,
        choices=range(1, 6),
        default=3,
        help="Velocidad del escaneo: T1 a T5"
    )

    args = parser.parse_args()

    # Configuracion de velocidad
    timing = TIMING_LEVELS[args.T]
    workers = timing["workers"]
    timeout = timing["timeout"]

    # Obtener los puertos
    try:
        ports = list(get_ports(args))
    except ValueError as error:
        parser.error(str(error))

    # Resolver el objetivo
    try:
        target_ip = socket.gethostbyname(args.target)
    except socket.gaierror:
        parser.error("No se pudo resolver el objetivo.")

    print("=" * 45)
    print("                 M-NMAP")
    print("=" * 45)

    print(f"Objetivo: {args.target} ({target_ip})")
    print(f"Puertos a analizar: {len(ports)}")
    print(f"Velocidad: T{args.T}")
    print(f"Trabajadores simultaneos: {workers}")

    if args.version_detection:
        print("Deteccion de versiones: Activada")

    print("\nIniciando escaneo...\n")

    start_time = time.time()
    open_ports = []

    # Escaneo concurrente
    with concurrent.futures.ThreadPoolExecutor(
        max_workers=workers
    ) as executor:

        futures = {
            executor.submit(
                scan_port,
                target_ip,
                port,
                timeout,
                args.version_detection
            ): port
            for port in ports
        }

        for future in concurrent.futures.as_completed(futures):
            port = futures[future]

            try:
                result = future.result()

                if result:
                    open_ports.append(result)

                    print(
                        f"[+] {port}/tcp OPEN "
                        f"{result['service']}"
                    )

                    if args.version_detection:
                        print(
                            f"    Version: {result['version']}"
                        )

                elif args.verbose:
                    print(f"[v] Puerto {port}: cerrado o filtrado")

            except Exception as error:
                if args.verbose:
                    print(f"[!] Puerto {port}: {error}")

    # Resumen final
    elapsed = time.time() - start_time

    print("\n" + "=" * 45)
    print("             RESULTADOS")
    print("=" * 45)

    if open_ports:
        open_ports.sort(key=lambda item: item["port"])

        print(
            f"{'PORT':<12}{'STATE':<12}{'SERVICE':<15}"
        )

        for item in open_ports:
            print(
                f"{item['port']:<12}"
                f"{item['state']:<12}"
                f"{item['service']:<15}"
            )

    else:
        print("No se encontraron puertos abiertos.")

    print(f"\nPuertos abiertos: {len(open_ports)}")
    print(f"Tiempo total: {elapsed:.2f} segundos")
    print("Escaneo finalizado.")


if __name__ == "__main__":
    main()
