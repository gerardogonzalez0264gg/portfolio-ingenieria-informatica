import time, winsound

def reloj(segundos, mensaje):

    for i in range(segundos, 0,-1):
        print(f"Tiempo de {mensaje} quedan {i} segundos", end="\r")
        time.sleep(1)

    winsound.PlaySound("alarma.wav", winsound.SND_FILENAME)

while True:
    reloj(1800,"Estudio")
    reloj(300,"Descanso")