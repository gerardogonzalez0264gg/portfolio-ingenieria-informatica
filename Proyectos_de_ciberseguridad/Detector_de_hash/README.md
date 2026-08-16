# Detector de hash

Esta herramienta sirve para identificar de forma aproximada el tipo de hash, dependiendo de tres valores:

1. **Valor hex**
    
2. **El largo de la cadena**
    
3. **El valor del prefijo**
    

La idea principal de la herramienta es que al ingresar una cadena de texto, la herramienta pueda identificar algunos patrones que tiene esa cadena, para así poder asignarle un posible tipo de hash.

Para eso cree una serie de funciones y valores que ayudan a realizar la identificación. Por ejemplo, `Valor_Largo` es un diccionario que, en base a una clave que representa la cantidad de caracteres del texto, devuelve el posible tipo de hash que cumple con esas características.

Por ejemplo:

```python
Valor_Largo = {
    32: "MD5",
    40: "SHA-1",
    64: "SHA-256",
    128: "SHA-512",
}
```

De esta forma, si el texto ingresado tiene 32 caracteres y además todos sus caracteres son hexadecimales, el programa indicará que probablemente sea un MD5.

También está la función `es_hex()`, que sirve para comprobar si todos los caracteres ingresados son valores hexadecimales. Para esto se comprueba que los caracteres estén dentro de:

```text
0123456789abcdefABCDEF
```

Otra parte es `Valor_Prefijo`, que contiene algunos prefijos que son utilizados por ciertos tipos de hash. Por ejemplo:

```python
Valor_Prefijo = [
    ("$2b$", "bcrypt"),
    ("$argon2id$", "Argon2id"),
    ("$6$", "SHA-512 crypt"),
]
```

La herramienta revisa si el texto comienza con alguno de estos prefijos y, si encuentra uno, devuelve el tipo de hash que probablemente corresponde.

Una vez que se ingresa el valor, la función `identificador()` es la encargada de hacer el análisis. Primero elimina los espacios que puedan existir al principio y al final del texto.

Después comprueba si se ingresó algún dato. Si no se ingresó nada, devuelve:

```text
Ingresa algo para identificar
```

Luego revisa los prefijos y después comprueba si el texto ingresado está compuesto por caracteres hexadecimales. Si es hexadecimal, revisa el largo de la cadena para compararlo con los valores que están en `Valor_Largo`.

Si el largo coincide con alguno de los valores conocidos, devuelve algo como:

```text
Probablemente es: MD5
```

Si el texto es hexadecimal, pero su largo no coincide con ninguno de los valores que tengo registrados, devuelve:

```text
Es hex (X), pero no lo identifico
```

Y finalmente, si el texto no cumple con los parámetros que utiliza el programa, devuelve:

```text
No pude identificarlo
```

## Importante

La herramienta no puede saber con total seguridad qué tipo de hash es solamente mirando su formato. Lo que hace es comparar algunos patrones que son conocidos, como el valor hexadecimal, el largo de la cadena y los prefijos.

Por ejemplo, si una cadena tiene 32 caracteres hexadecimales, el programa dirá que **probablemente es MD5**, pero eso no significa que sea un MD5 con total seguridad.

## Ejemplo de uso

Al ejecutar el programa, se ingresa el hash:

```text
Ingresa el hash: 5d41402abc4b2a76b9719d911017c592
```

Y el programa devolverá:

```text
Probablemente es: MD5
```

## Objetivo del proyecto

La idea de este proyecto es crear una herramienta sencilla que permita identificar posibles tipos de hash mediante algunos patrones básicos, como el largo de la cadena, si contiene valores hexadecimales y si tiene algún prefijo conocido.
