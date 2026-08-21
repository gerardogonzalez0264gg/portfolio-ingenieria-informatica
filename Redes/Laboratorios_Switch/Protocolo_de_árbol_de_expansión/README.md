# Red STP: Explicación del protocolo Spanning Tree y su configuración.

La finalidad de esto es optimizar la recuperación de la red mediante la designación del Root Bridge y el uso de Rapid PVST+.

### **Task 1: Forzar al Switch 1 a ser el Root Bridge (Puente Raíz)**

Plaintext

```
Switch(config)#spanning-tree vlan 1 priority 0
-- o bien --
Switch(config)#spanning-tree vlan 1 root primary
```

- **¿Qué se hace?** Le asigna la prioridad más baja (0 o rango primario) a la VLAN 1 en el Switch 1.
    
- **¿Para qué sirve?** El algoritmo STP elige como **Root Bridge** (el switch "jefe" o central de la topología) al switch que tenga la prioridad más baja. Esto asegura que el tráfico pase de forma predecible y eficiente a través del Switch 1.
    

### **Task 2: Activar Rapid Spanning Tree (RSTP)**

Plaintext

```
Switch(config)#spanning-tree mode rapid-pvst
```

- **¿Qué se hace?** Cambia el protocolo de Spanning Tree estándar (802.1D) a **Rapid PVST+** (Per-VLAN Spanning Tree Plus basándome en 802.1w) en todos los switches.
    
- **¿Para qué sirve?** Acelera masivamente el tiempo de recuperación de la red ante fallos de enlaces o switches. Con el STP tradicional la red tarda entre 30 y 50 segundos en reajustarse; con Rapid PVST+ se logra casi al instante (en un par de segundos).

SPT: Es un protocolo de Capa 2 que **bloquea puertos y enlaces redundantes** en un switch para evitar bucles infinitos de red.

**32768** = La prioridad "neutra" que traen los switches por defecto para STP.
