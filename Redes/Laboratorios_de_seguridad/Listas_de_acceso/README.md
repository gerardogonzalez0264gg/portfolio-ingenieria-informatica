# Configurar una ACL (lista de control de acceso) en Packet Tracer

En este laboratorio configuramos **listas de control de acceso (ACLs)** en Packet Tracer para filtrar el tráfico de red: bloqueamos todo el acceso de un host con una ACL estándar y restringimos solo sus consultas DNS con una ACL extendida.

ACL: Control de trafico

- **Standard access list:** Se basa **únicamente en la IP de origen** y es más fácil de configurar.
    
- **Extended access-list:** Se basa en la **IP de origen, IP de destino, protocolos y puertos**, entregando una mayor cantidad de filtros para el control del tráfico.

- **De 1 a 99 (y 1300-1999):** Reservados para **ACLs Estándar** (solo filtran por IP de origen).
    
- **De 100 a 199 (y 2000-2699):** Reservados para **ACLs Extendidas** (filtran por IP de origen, IP de destino, protocolo y puerto).

