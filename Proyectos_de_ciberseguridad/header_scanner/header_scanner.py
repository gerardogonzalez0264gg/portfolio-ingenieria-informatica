import requests

cabeceras = [
    {"header": "Strict-Transport-Security", "gravedad": "alta"},
    {"header": "Content-Security-Policy",    "gravedad": "alta"},
    {"header": "X-Content-Type-Options",     "gravedad": "media"},
    {"header": "X-Frame-Options",            "gravedad": "media"},
    {"header": "Referrer-Policy",            "gravedad": "baja"},
]

valor = {"alta": 30, "media": 15, "baja": 5}

def escanear(url):
    respuesta = requests.get(url, timeout=10)
    headers_recibidos = respuesta.headers  

    resultados = []
    for regla in cabeceras:
        nombre = regla["header"]
        presente = nombre in headers_recibidos
        resultados.append({
            "header": nombre,
            "gravedad": regla["gravedad"],
            "presente": presente,
        })
    return resultados, respuesta.status_code

def calcular_nota(resultados):
    total_posible = sum(valor[r["gravedad"]] for r in resultados)
    ganado = sum(valor[r["gravedad"]] for r in resultados if r["presente"])

    score = round((ganado / total_posible) * 100)

    if score >= 90: nota = "A"
    elif score >= 80: nota = "B"
    elif score >= 70: nota = "C"
    elif score >= 60: nota = "D"
    else: nota = "F"

    return score, nota

if __name__ == "__main__":
    url = input("URL a escanear (con http:// o https://): ")
    resultados, status = escanear(url)
    score, nota = calcular_nota(resultados)

    print(f"\nRespuesta HTTP: {status}")
    print("-" * 40)
    for r in resultados:
        estado = "presente" if r["presente"] else "falta"
        print(f"{r['header']:30} {estado}")

    print("-" * 40)
    print(f"Puntaje: {score}/100 — Nota: {nota}")