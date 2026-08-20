# Configuración de VTP en Cisco Packet Tracer

El objetivo es ver cómo las VLANs creadas en el servidor se replican automáticamente en los clientes, mientras que el switch transparente las ignora y solo deja pasar la información hacia el resto.

VTP (Protocolo de troncalización virtual): Sincroniza y administra VLANs en toda la red de forma centralizada

**VTP server:**  Crea, modifica o elimina VLANs y distribuye los cambios al resto.

**VTP client:** No permite cambios locales; solo recibe y aplica la configuración del Servidor.

VTP transparent: Pasa de la sincronización; no aplica los cambios pero los reenvía a otros switches.
