# Una lista tiene varios objetos
# Observacion en una lista se puede almacenar diferentes tipos de objetos

numeros=[1,2,3,4,5,6,7,8,]
print(numeros)

#Buscamos un valor especifico de una lista
print(numeros[1])

#Imprimir los elementos de la lista en reversa
print(numeros[::-1])

#Incluir elementos a la lista
numeros.append(11)
print(numeros)

#Eliminar elementos de una lista, segun el indice que indiquemos
numeros.pop(0)
print(numeros)

#Recorrer elementos de una lista
for numero in numeros:
    print(numero)
