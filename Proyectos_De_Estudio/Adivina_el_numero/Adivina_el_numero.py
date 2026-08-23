import random,string

numero = 0
intento=0

print("Estas en un juego de adivinar el numero")

aleatorio = int(random.choice(string.digits))

while numero != aleatorio:

    numero= int(input("Ingresa un numero:"))
    intento+=1

    if numero > aleatorio:
        print("El numero es menor")
    elif numero < aleatorio:
        print("El numero es mayor")
    else:
        print(f"LE ATINASTEE!!!!, el numero era {aleatorio}")
        print(f"Le atinaste al {intento}° intento")
        

    