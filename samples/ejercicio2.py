
estudiante = {
    "matricula": "200527",
    "nombre": "Crystian",
    "apellido": "Suarez",
    "edad": 20,
    "cuatrimestre": "5",
    "promedio": "10",
}

lista=[estudiante]

while True:
    print('Menu\n 1.-Insertar\n 2.-Buscar\n 3.-Mostrar Datos\n 4.-Actualizar\n 5.-Eliminar\n 6.-Salir')
    opt=int(input('Select a option: '))
    if opt == 1:
        est={}
        est["matricula"] = input("Ingrese la matricula del estudiante: ")
        est["nombre"] = input("Ingrese el nombre del estudiante: ")
        est["apellido"] = input("Ingrese el apellido del estudiante: ")
        est["edad"] = int(input("Ingrese la edad del estudiante: "))
        est["cuatrimestre"] = input("Ingrese el cuatrimestre del estudiante: ")
        est["promedio"] = input("Ingrese el promedio del estudiante: ")
        print(f" \nEstudiante Agregado:\n {est}\n")
        lista.append(est)

    elif opt == 2:
        matricula = input("Ingrese la matricula del estudiante para encontrarlo: ")
        for e in lista:
            if e["matricula"] == matricula:
                print("Estudiante Encontrado: \n", e)

    elif opt == 3:
        print("Estudiantes Registrados:\n")
        for n in lista:
            print("\n---",n)

    elif opt == 4: #Actualizar
        matricula = input(" \nIngrese la matricula del estudiante para Actualizar informacion: ")
        for e in lista:
            if e["matricula"] == matricula:
                e["matricula"] = input("Ingrese la matricula del estudiante: ")
                e["nombre"] = input("Ingrese el nombre del estudiante: ")
                e["apellido"] = input("Ingrese el apellido del estudiante: ")
                e["edad"] = int(input("Ingrese la edad del estudiante: "))
                e["cuatrimestre"] = input("Ingrese el cuatrimestre del estudiante: ")
                e["promedio"] = input("Ingrese el promedio del estudiante: ")
                print("Estudiante Actualizado:\n",e)

    elif opt == 5:
        matricula = input("Ingrese la matricula del estudiante para eliminar: ")
        for e in lista:
            if e["matricula"] == matricula:
                print(" \nEstudiante eliminado")
                lista.remove(e)

    elif opt == 6:
        print("Adios Humano. Te mostrare los registros de los estudiantes:")
        break
    else:
        print("Invalid option\n")




for index,n in enumerate(lista):
    print(f"\n---{index+1}--- {n}")