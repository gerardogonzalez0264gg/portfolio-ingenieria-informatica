# Configurar el banner MOTD y habilitarlo en las líneas Telnet

Configurar la dirección IP, descripción de interfaz y un mensaje de advertencia (MOTD) en el router para facilitar la administración del equipo y prevenir accesos no autorizados.

- **Banner:** Un aviso estático de advertencia o identificación que ves al acceder a un equipo.
    
- **MOTD:** Un banner temporal que se muestra inmediatamente antes de pedirte usuario y contraseña.
	
- VTY line: Cuando te conectas por SSH (puerto 22) al switch, la red te asigna **una de las líneas VTY libres** (por ejemplo, la `vty 0`). Si entra otra persona, usará la `vty 1`, y así sucesivamente.
