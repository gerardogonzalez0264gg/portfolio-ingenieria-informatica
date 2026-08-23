# GymTime RFID

## 📌 Descripción

**GymTime RFID** es un proyecto desarrollado para la asignatura de **Robótica**, cuyo objetivo es crear un sistema que permita organizar y controlar el uso de las máquinas de un gimnasio.

La idea principal del proyecto es funcionar como un **reloj de entrenamiento**, permitiendo controlar el tiempo de uso de cada máquina, las series y los períodos de descanso. De esta manera, se busca evitar que se generen largas filas o esperas innecesarias entre las personas que utilizan las máquinas del gimnasio.

## ⚙️ Funcionamiento

El sistema utiliza una tarjeta **RFID** para identificar al usuario. Una vez identificado, el usuario puede seleccionar la máquina que desea utilizar y configurar los parámetros de su entrenamiento, como el tiempo de cada serie, el tiempo de descanso y la cantidad de series.

La información se muestra mediante una **pantalla LCD**, mientras que los botones permiten interactuar con el sistema. Al finalizar los tiempos establecidos, el sistema utiliza un **buzzer** para avisar al usuario.

El proyecto fue desarrollado y probado mediante una simulación en **Wokwi** utilizando un ESP32 y diferentes componentes electrónicos.

## 🔧 Componentes utilizados

* ESP32
* Lector RFID RC522
* Tarjetas RFID
* Pantalla LCD 16x2 con I2C
* Botones
* LED
* Buzzer

## 🎯 Finalidad

La finalidad de **GymTime RFID** es mejorar la organización del uso de las máquinas dentro de un gimnasio, estableciendo tiempos de entrenamiento y descanso para cada usuario. Esto permite aprovechar mejor las máquinas disponibles y reducir la formación de filas.

El proyecto busca aplicar conocimientos de **robótica, programación y electrónica** para desarrollar una solución a una situación que puede presentarse en gimnasios.


🚀 **Ver y probar simulación en vivo:** [https://wokwi.com/projects/473156467651207169](https://wokwi.com/projects/473156467651207169)
