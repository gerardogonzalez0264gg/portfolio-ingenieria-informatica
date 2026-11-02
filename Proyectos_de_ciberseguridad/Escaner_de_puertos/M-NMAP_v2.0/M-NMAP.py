import socket
import argparse
import concurrent.futures
import time
import json
import ssl
from datetime import datetime


# Puertos comunes
COMMON_PORTS = [
    21, 22, 23, 25, 53, 80, 110, 135, 139,
    143, 443, 445, 993, 995, 3306, 3389,
    5432, 5900, 8080, 8443
]

# Configuracion de velocidad
TIMING_LEVELS = {
    1: {"workers": 5, "timeout": 2.0},
    2: {"workers": 15, "timeout": 1.5},
    3: {"workers": 50, "timeout": 1.0},
    4: {"workers": 100, "timeout": 0.7},
    5: {"workers": 200, "timeout": 0.5}
}


def get_ports(args):
    """Selecciona los puertos que se analizaran."""

    if args.all_ports:
        return list(range(1, 65536))

    if args.fast:
        return COMMON_PORTS

    if args.ports:
        selected_ports = set()

        for item in args.ports.split(","):
            if "-" in item:
                parts = item.split("-")

                if len(parts) != 2:
                    raise ValueError("Rango de puertos invalido.")

                first, last = map(int, parts)

                if first < 1 or last > 65535 or first > last:
                    raise ValueError("Rango de puertos invalido.")

                selected_ports.update(range(first, last + 1))

            else:
                port = int(item)

                if port < 1 or port > 65535:
                    raise ValueError("Puerto invalido.")

                selected_ports.add(port)

        return sorted(selected_ports)

    return list(range(1, 1001))


def identify_service(port):
    """Obtiene el nombre habitual asociado al puerto."""

    try:
        return socket.getservbyport(port, "tcp")
    except OSError:
        return "unknown"


def detect_version(target, port, timeout):
    """Intenta obtener informacion del servicio."""

    try:
        with socket.create_connection(
            (target, port), timeout=timeout
        ) as connection:

            connection.settimeout(timeout)

            # Conectar mediante TLS en puertos HTTPS habituales
            if port in (443, 8443):
                context = ssl.create_default_context()

                with context.wrap_socket(
                    connection,
                    server_hostname=target
                ) as secure_connection:

                    request = (
                        f"HEAD / HTTP/1.0\r\n"
                        f"Host: {target}\r\n\r\n"
                    )

                    secure_connection.sendall(request.encode())
                    banner = secure_connection.recv(1024)

            # Solicitud HTTP
            elif port in (80, 8000, 8080):
                request = (
                    f"HEAD / HTTP/1.0\r\n"
                    f"Host: {target}\r\n\r\n"
                )

                connection.sendall(request.encode())
                banner = connection.recv(1024)

            else:
                # Intentar recibir informacion del servicio
                banner = connection.recv(1024)

            if banner:
                return banner.decode(
                    "utf-8", errors="replace"
                ).strip().replace("\r", " ").replace("\n", " ")[:150]

    except (OSError, TimeoutError, ssl.SSLError):
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
                version = "No analizada"

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


def save_report(results, target, elapsed, output, file_format):
    """Guarda los resultados en TXT o JSON."""

    report_data = {
        "target": target,
        "date": datetime.now().isoformat(timespec="seconds"),
        "scan_duration": round(elapsed, 2),
        "open_ports": results
    }

    if file_format == "json":
        with open(output, "w", encoding="utf-8") as file:
            json.dump(
                report_data,
                file,
                indent=4,
                ensure_ascii=False
            )

    else:
        with open(output, "w", encoding="utf-8") as file:
            file.write("M-NMAP - INFORME DE ESCANEO\n")
            file.write("=" * 40 + "\n")
            file.write(f"Objetivo: {target}\n")
            file.write(f"Fecha: {report_data['date']}\n")
            file.write(f"Duracion: {elapsed:.2f} segundos\n\n")

            if results:
                for item in results:
                    file.write(
                        f"{item['port']}/tcp - "
                        f"{item['state']} - "
                        f"{item['service']} - "
                        f"{item['version']}\n"
                    )
            else:
                file.write("No se encontraron puertos abiertos.\n")

    print(f"\nInforme guardado en: {output}")


def main():
    parser = argparse.ArgumentParser(
        description="M-NMAP 3.0 - Escaner de puertos TCP"
    )

    parser.add_argument(
        "target",
        help="Direccion IP o nombre del objetivo"
    )

    scan_group = parser.add_mutually_exclusive_group()

    scan_group.add_argument(
        "-p", "--ports",
        help="Puertos especificos. Ejemplo: 22,80,1-100"
    )

    scan_group.add_argument(
        "-p-",
        dest="all_ports",
        action="store_true",
        help="Analizar todos los puertos TCP"
    )

    scan_group.add_argument(
        "-F", "--fast",
        action="store_true",
        help="Analizar puertos comunes"
    )

    parser.add_argument(
        "-v", "--verbose",
        action="store_true",
        help="Mostrar informacion detallada"
    )

    parser.add_argument(
        "-sV",
        dest="version_detection",
        action="store_true",
        help="Intentar detectar informacion de versiones"
    )

    parser.add_argument(
        "-T",
        type=int,
        choices=range(1, 6),
        default=3,
        help="Velocidad del escaneo: T1 a T5"
    )

    parser.add_argument(
        "-o",
        "--output",
        help="Nombre del archivo para guardar el informe"
    )

    parser.add_argument(
        "--format",
        choices=["txt", "json"],
        default="txt",
        help="Formato del informe"
    )

    args = parser.parse_args()

    # Configurar velocidad
    timing = TIMING_LEVELS[args.T]
    workers = timing["workers"]
    timeout = timing["timeout"]

    # Seleccionar puertos
    try:
        ports = get_ports(args)
    except ValueError as error:
        parser.error(str(error))

    # Resolver el objetivo
    try:
        target_ip = socket.gethostbyname(args.target)
    except socket.gaierror:
        parser.error("No se pudo resolver el objetivo.")

    print("=" * 45)
    print("                 M-NMAP 3.0")
    print("=" * 45)

    print(f"Objetivo: {args.target} ({target_ip})")
    print(f"Puertos a analizar: {len(ports)}")
    print(f"Velocidad: T{args.T}")
    print(f"Trabajadores simultaneos: {workers}")

    if args.version_detection:
        print("Deteccion de versiones: Activada")

    print("\nIniciando escaneo...\n")

    start_time = time.perf_counter()
    open_ports = []
    completed = 0
    progress_step = max(1, len(ports) // 20)

    # Ejecutar escaneo concurrente
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
            completed += 1

            try:
                result = future.result()

                if result:
                    open_ports.append(result)

                    print(
                        f"[+] {port}/tcp ABIERTO "
                        f"- {result['service']}"
                    )

                    if args.version_detection:
                        print(f"    Informacion: {result['version']}")

                elif args.verbose:
                    print(f"[v] Puerto {port}: cerrado o filtrado")

            except Exception as error:
                if args.verbose:
                    print(f"[!] Puerto {port}: {error}")

            # Mostrar progreso
            if completed % progress_step == 0 or completed == len(ports):
                percentage = (completed / len(ports)) * 100

                print(
                    f"\rProgreso: {percentage:.1f}% "
                    f"({completed}/{len(ports)})",
                    end="",
                    flush=True
                )

    elapsed = time.perf_counter() - start_time
    open_ports.sort(key=lambda item: item["port"])

    # Mostrar resultados
    print("\n\n" + "=" * 45)
    print("             RESULTADOS")
    print("=" * 45)

    if open_ports:
        print(f"{'PUERTO':<12}{'ESTADO':<12}{'SERVICIO':<15}")

        for item in open_ports:
            print(
                f"{item['port']:<12}"
                f"{item['state']:<12}"
                f"{item['service']:<15}"
            )

            if args.version_detection:
                print(f"  Informacion: {item['version']}")

    else:
        print("No se encontraron puertos abiertos.")

    print(f"\nPuertos abiertos: {len(open_ports)}")
    print(f"Tiempo total: {elapsed:.2f} segundos")
    print("Escaneo finalizado.")

    # Guardar informe si se solicito
    if args.output:
        save_report(
            open_ports,
            target_ip,
            elapsed,
            args.output,
            args.format
        )


if __name__ == "__main__":
    main()