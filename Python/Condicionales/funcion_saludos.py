def conversacion(mensaje):
    print('Hola')
    print('como estas')
    print(mensaje)
    print('Adios')

opcion = int(input('Elige una opcion entre 1, 2 y 3: '))
if opcion ==1:
    conversacion('Elegiste la opcion 1.')
elif opcion == 2:
    conversacion('Elegsite la opcion 2.')
elif opcion ==3:
    conversacion('Elegiste la opcion 3.')
else:
    conversacion('Elegiste una opcion incorrecta')