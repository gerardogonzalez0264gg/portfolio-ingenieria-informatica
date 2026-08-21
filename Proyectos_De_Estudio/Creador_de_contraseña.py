import random, string

longitud = int(input("Ingrese la longitud de la contraseña: "))

aleatorio = string.ascii_letters + string.digits + string.punctuation

contraseña = ""

for i in range(longitud):
    contraseña += random.choice(aleatorio)

print(f"contraseña generada: {contraseña}")