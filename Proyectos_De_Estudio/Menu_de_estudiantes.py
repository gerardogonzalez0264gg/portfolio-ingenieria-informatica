estudiante = {

    "alonso": { "edad":13, "nota":4.5},
    "juan": {"edad": 11, "nota":5.4},
    "sofia": {"edad":42, "nota":7.0},
    "ana": {"edad":23, "nota":5.3},

}

while True:

    print("MENU")
    print("1) Agregar estudiante")
    print("2) Ver estudiantes")
    print("3) Buscar estudiante")
    print("4) Eliminar estudiante")
    print("5) Salir")
    try:
        numero=int(input("Ingrese un numero del menu: "))
    except:
        print("El ingreso debe de ser un numero del menu")
        continue

    if numero == 1:
        nombre=input("Ingrese el nombre: ")
        edad=int(input("Ingrese la edad: "))
        nota=float(input("Ingrese su nota: "))

        estudiante[nombre]={"edad":edad, "nota":nota}

        print("Se agrego existosamente al usuario!!!")
    elif numero==2:
        for nombre, datos in estudiante.items():
            print(f"Nombre: {nombre}")
            print(f"Edad: {datos['edad']}")
            print(f"Nota: {datos['nota']}\n")
    elif numero==3:
        nombre=input("Ingrese el nombre del estudiante que desea conocer: ")
        if nombre in estudiante:
            print(estudiante[nombre])
        else:
            print("El estudiante no existe")
    elif numero==4:
        nombre=input("Ingrese el nombre del estudiante que quiere eliminar: ")
        if nombre in estudiante:      
            del estudiante[nombre]
            print(f"El estudiante {nombre} a sido eliminado!!!")
        else:
            print(f"El nombre del estudiante {nombre}, no existe")
    elif numero==5:
        print("Se a salido exitosamente!!!")
        break
    else:
        print("Opcion no valida")



