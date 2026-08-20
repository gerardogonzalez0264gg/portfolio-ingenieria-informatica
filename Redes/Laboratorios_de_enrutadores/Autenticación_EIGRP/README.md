# Autenticación EIGRP (router-2)

### Configurar el Protocolo EIGRP

- **`router eigrp [ID]`:** Activa el protocolo de enrutamiento dinámico. El ID (por ejemplo, `10`) debe ser el mismo en todos los routers de la red para que se hablen.
    
- **`network [Dirección_Red]`:** Le dice al protocolo qué redes tiene conectadas el router para que se las enseñe a sus vecinos.
    

### Cifrado y Autenticación MD5 (Seguridad)

- **`key chain [Nombre]`:** Crea el "llavero" virtual para guardar contraseñas.
    
- **`key [Número]`:** Crea una llave específica dentro de ese llavero (ej. `key 1`).
    
- **`key-string [Contraseña]`:** Define la palabra secreta real de esa llave (ej. `Packet`).
    
- **`ip authentication mode eigrp [ID] md5`:** _(Se aplica dentro de la interfaz)_. Obliga al puerto a usar cifrado MD5 para que nadie pueda robarse la contraseña del cable.
    
- **`ip authentication key-chain eigrp [ID] [Nombre_Llavero]`:** _(Se aplica dentro de la interfaz)_. Le dice al puerto qué llavero debe usar para validar la seguridad.
    

### Comandos de Verificación (Diagnóstico)

- **`show ip eigrp neighbors`:** Muestra la lista de routers vecinos de confianza que pasaron la prueba de la contraseña.
    
- **`show ip route`:** Muestra la tabla de enrutamiento. Las redes aprendidas de forma segura a través de EIGRP aparecen marcadas con una **`D`**.
