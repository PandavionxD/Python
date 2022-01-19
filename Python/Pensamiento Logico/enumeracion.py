#Enumeracion exhaustiva
objetivo = int(input('Escribe aqui el numero para saber si tiene raiz cuadrada: '))
contador= 0
while contador**2<objetivo:
    contador+=1
if contador**2==objetivo:
    print(f'Este programa tiene raiz cuadrada y es {contador}')
else:
    print('Este programa no tiene raiz cuadrada.')