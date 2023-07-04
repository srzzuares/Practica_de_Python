desarrollador= {
    "nombre": "Juan",
    "apellido": "Perez",
    "edad": 20,
    "cursos": [
        "Python",
        "Java",
        "C#"
    ]
}

estudiante = {
    "macricula": "200527",
    "nombre": "Crystian",
    "apellido": "Suarez",
    "edad": 20,
    "cuatrimestre": "5",
    "promedio": "10",
    "cursos": [
        "Python",
        "Java",
        "C#"
    ]
}


print(estudiante, desarrollador)


for n in estudiante: #imprime el contenido de las keys
    print(n)
for nn in estudiante: #Imprime  los valores de estudiante
    print("\n1---",estudiante[nn])

for nnn in estudiante: #Imprime los valores
    print("\n2---",estudiante[nnn])



print(estudiante.keys()) #imprime el contenido de las keys
print(estudiante.values()) #imprime el contenido de las values de estudiant valores
print(estudiante.items())  #imprime el contenido de las items de estudiant elements
