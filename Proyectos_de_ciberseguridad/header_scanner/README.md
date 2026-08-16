# Headers Scanner HTTP

Este es un proyecto simple hecho en Python para revisar algunas cabeceras de seguridad de una página web.

## ¿Cómo funciona?

El programa:

1. Pide una URL.
2. Hace una petición a la página.
3. Revisa algunas cabeceras de seguridad.
4. Comprueba cuáles están presentes y cuáles faltan.
5. Da puntos según la importancia de cada cabecera.
6. Calcula un puntaje de 0 a 100 y una nota de A a F.

Las cabeceras tienen diferentes valores dependiendo de su gravedad:

- **Alta:** 30 puntos
- **Media:** 15 puntos
- **Baja:** 5 puntos

## Ejemplo

```text
URL a escanear: [https://github.com](https://github.com)

Respuesta HTTP: 200
----------------------------------------
Strict-Transport-Security       presente
Content-Security-Policy         presente
X-Content-Type-Options          presente
X-Frame-Options                 presente
Referrer-Policy                 presente
----------------------------------------
Puntaje: 100/100 — Nota: A
