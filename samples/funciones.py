################################# Multiplicacion
def f(x=1,y=1):
    return y*x
#y = f(30,2)
#print(y) # 60


################################ Hola Nombre
def di_hola(nombre="Humano"):
    print("Hola", nombre)
di_hola("Crystian\n")

################################ Resta
def resta(a=0, b=0):
    return a-b
# print(resta(5, 3)) # 2
################################ division
def divicion(a=0, b=0):
    return a/b
# print(divicion(5, 3)) # 2

################################ Suma
def suma(a=0, b=0):
    return a+b
#print(suma(5,5,3)) # 13  suma()

###############################
def sumas(*numeros):
    print(type(numeros))
    # <class 'tuple'>
    total = 0
    for n in numeros:
        total += n
    return total
print(sumas(1, 3, 5, 4)) # 13
'''
suma(6) # 6
suma(6, 4, 10) # 20
suma(6, 4, 10, 20, 4, 6, 7) # 57
'''

###############################
def suma3(**kwargs):
    suma3 = 0;
    for key, value in kwargs.items():
        print(key, value)
        suma3 += value
    return suma3

#print(suma(a=5, b=20, c=23, d=2)) # 48

###############################
x = int(input("Ingrese el primer numero: "))
y = int(input("Ingrese el segundo numero: "))
print("Menu\n1.-Multiplicacion\n2.-Suma\n3.-Resta\n4.-multiply en lista o tupla\n5.-divicion")
opt = int(input("Select a number: "))
if opt == 1:
    print(f(x,y))
elif opt == 2:
    print(suma(x,y))
elif opt == 3:
    print(resta(x,y))
elif opt == 4:
    print(sumas(x,y))
elif opt == 5:
    print(divicion(x,y))
