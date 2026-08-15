def hex(texto):
    caracteres = "0123456789abcdefABCDEF"
    return all(a in caracteres for a in texto)  

Valor_Largo = {
    32: "MD5",
    40: "SHA-1",
    64: "SHA-256",
    128: "SHA-512",
}

Valor_Prefijo = [
    ("$2b$", "bcrypt"),
    ("$argon2id$", "Argon2id"),
    ("$6$", "SHA-512 crypt"),
]

def identificador(texto):
    texto = texto.strip()  

    if not texto:
        return "Ingresa algo para identificar"

    for prefijo, nombre in Valor_Prefijo:
        if texto.startswith(prefijo):
            return f"Probablemente es: {nombre}"

    if hex(texto):
        largo = len(texto)
        if largo in Valor_Largo:
            return f"Probablemente es: {Valor_Largo[largo]}"
        return f"Es hex ({largo}), pero no lo identifico"

    return "No pude identificarlo"

if __name__ == "__main__":
    entrada = input("Ingresa el hash: ")
    resultado = identificador(entrada)
    print(resultado)