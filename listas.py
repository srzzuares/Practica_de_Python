list = [1,2,3,4,2,2]
print(list)
'''for lista in list:
    print(lista) #imprimer cada eleento que tiene
'''
list1 = [1, "Hola", 3.67, [1, 2, 3]] #El contenido de la tupla o lista
print(list1) #Ver lo que contiene la lista
print(list1[-2]) # Para ver el penultimo elemento

'''list1[3]=1234321 #Para Actualizar un dato
print(list1) # checamos si se actualizo

for a, b in zip(list,list1):  # Juntar dos listas
    print(f'{a} :: {b}  junta dos listas temporales con for in---')
'''

'''list.append(5) #Agrega el elemento al final
list1.append(5)
print(f'{list} :: {list1}  agrega elementos ---')'''

#list.clear() para limpiar la lista

'''list.extend(list1) #para unir listas
print(f'{list} Unir listas---')
'''
print(f'{list.index(3)} ---')
