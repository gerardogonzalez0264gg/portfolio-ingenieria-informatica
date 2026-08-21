# Líneas VTY 0-4, 5-15 y 0-15 en Cisco

Objetivo: Comprender y configurar el rango de líneas VTY (0-4, 5-15 o 0-15) en equipos Cisco para gestionar el número de conexiones remotas simultáneas y asegurar su acceso mediante contraseñas.

--------

Las líneas VTY para acceso remoto (Telnet) en Cisco: `line vty 0 4` permite 5 conexiones simultáneas, `5 15` agrega 11 más y `0 15` habilita las 16 totales. Configure la  contraseña (en texto plano o tipo 7) con line vty 0 (una sola conexión).
