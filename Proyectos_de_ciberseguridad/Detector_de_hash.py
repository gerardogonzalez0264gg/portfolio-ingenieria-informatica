# Comprueba si el texto tiene solo valores hexadecimales
def es_hex(texto):
    caracteres = "0123456789abcdefABCDEF"
    return all(a in caracteres for a in texto)


# Relaciona del largo con los algoritmos que se conocen
Valor_Largo = {
    32: "MD5",
    40: "SHA-1",
    64: "SHA-256",
    128: "SHA-512",
}


# Prefijos utilizados para los hash.
Valor_Prefijo = [
    ("$2b$", "bcrypt"),
    ("$argon2id$", "Argon2id"),
    ("$6$", "SHA-512 crypt"),
]


def identificador(texto):
    # Elimina espacios al principio y al final
    texto = texto.strip()

    # Comprueba si es que se ingreso algo
    if not texto:
        return "Ingresa algo para identificar"

    # Primero identificamos en base al prefijos
    for prefijo, nombre in Valor_Prefijo:
        if texto.startswith(prefijo):
            return f"Probablemente es: {nombre}"

    # Comprueba si es hexadecimal
    if es_hex(texto):
        largo = len(texto)

        # Indentifica según la longitud.
        if largo in Valor_Largo:
            return f"Probablemente es: {Valor_Largo[largo]}"

        # Es hexadecimal, pero su longitud no coincide con las conocidas.
        return f"Es hex ({largo}), pero no lo identifico"

    # No coicide con los parametros
    return "No pude identificarlo"


# Entrada del programa
if __name__ == "__main__":
    entrada = input("Ingresa el hash: ")
    resultado = identificador(entrada)
    print(resultado)