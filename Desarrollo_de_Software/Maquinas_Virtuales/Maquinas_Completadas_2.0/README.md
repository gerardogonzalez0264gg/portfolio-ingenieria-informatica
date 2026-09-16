# 🖥️ Máquinas Virtuales 2.0

Versión mejorada del proyecto **Máquinas Completadas**, creado para registrar y documentar máquinas virtuales resueltas durante el aprendizaje de ciberseguridad.

## 🎯 Objetivo

El objetivo del proyecto es **registrar, organizar y documentar el aprendizaje obtenido al resolver máquinas virtuales de ciberseguridad**, permitiendo consultar posteriormente las herramientas utilizadas, las vulnerabilidades encontradas y el proceso de resolución de cada máquina.

## 🚀 Mejoras de la versión 2.0

### 🔎 Búsqueda mejorada

* Permite buscar utilizando solo una parte del nombre de la máquina.
* No diferencia entre mayúsculas y minúsculas.
* Permite presionar `Enter` para realizar la búsqueda.
* Se agregó la opción **"Ver todas"** para volver a mostrar todas las máquinas.

### 📖 Walkthroughs

Se agregó la posibilidad de documentar el proceso de resolución de cada máquina mediante walkthroughs.

Los walkthroughs permiten explicar paso a paso:

* Enumeración.
* Vulnerabilidades encontradas.
* Explotación.
* Escalada de privilegios.
* Técnicas y herramientas utilizadas.

Los walkthroughs se muestran dentro de la misma página mediante una ventana modal, sin necesidad de salir del sitio.

### 🧩 Código más modular

El código JavaScript fue reorganizado para separar las diferentes responsabilidades mediante funciones:

* `mostrar()` → carga los datos de las máquinas.
* `crearTarjeta()` → crea las tarjetas.
* `renderizarLista()` → muestra las máquinas.
* `buscar()` → realiza las búsquedas.
* `mostrarTodas()` → muestra nuevamente todas las máquinas.
* `abrirWalkthrough()` → abre el walkthrough.
* `cerrarWalkthrough()` → cierra el walkthrough.

### 📝 Soporte para Markdown

Se incorporó `Marked.js` para poder escribir los walkthroughs utilizando Markdown y mostrarlos con formato dentro de la página.

### 🎨 Mejoras visuales

* Nueva ventana modal para los walkthroughs.
* Nuevos botones de interacción.
* Mejor presentación del contenido.
* Soporte para código, títulos, enlaces e imágenes dentro de los walkthroughs.
* Tarjetas con un tamaño más flexible.

### ➕ Nuevas máquinas

La versión 2.0 incorpora nuevas máquinas al proyecto, aumentando el contenido disponible para documentar y consultar.

## 📌 Comparación con la versión 1.0

| Característica        | Máquinas Completadas 1.0   |  Máquinas 2.0     |
| --------------------- | ------------------------   |  ---------------- |
| Catálogo de máquinas  | ✅                        | ✅                | 
| Búsqueda              | Básica                     | Mejorada          |
| Búsqueda parcial      | ❌                        | ✅                |
| Mayúsculas/minúsculas | Coincidencia exacta        | No importa        |
| Mostrar todas         | ❌                        | ✅                |
| Búsqueda con Enter    | ❌                        | ✅                |
| Walkthroughs          | ❌                        | ✅                |
| Ventana modal         | ❌                        | ✅                |
| Markdown              | ❌                        | ✅                |
| Código modular        | Básico                    | Mejor organizado |
| Máquinas registradas  | 20                       | 23               |

