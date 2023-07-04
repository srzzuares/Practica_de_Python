'''while True:
    numero = int(input())
    if numero == 0:
        break;'''

'''
Mejor Promedio
Peor Promedio
Promedio Grupal
Promedio Ordenados
'''

promedios = []
bestPro = []
failPro =[]
canPro = 0
ProFinal = 0

while True:
    canPro = int(input('Promedio: '))
    if canPro == 0:
        break;
    promedios.append(canPro)
    if canPro > 9:
        bestPro.append(canPro)
    if canPro < 4:
        failPro.append(canPro)
    ProFinal += canPro

promedios.sort(reverse=True)
final= ProFinal / len(promedios)

print(f'Son tu promedios {promedios}')
print(f'\n\nMejor Promedio ---{bestPro}')
print(f'\n\nPeor Promedio --------{failPro}')
print(f'\n\nPromedio Grupal: ........ {final}')

for n in promedios:
    print(f'-----{n}')






