def imprimir_mensaje():
    print('Mensaje Especial: ')
    print('Estoy aprendiendo a usar funciones.')

# LLAMO A LAS FUNCIONEMS
imprimir_mensaje()
imprimir_mensaje()
imprimir_mensaje()

def mensaje(msj):
    print('''
Hola!
como estas'''
,msj ,'''
adios''')
print('Escoje una opcion del 1-3.')
opcion =int(input('opcion: '))
if opcion==1:
    mensaje('escojiste la opcion 1')
elif opcion==2:
    mensaje('escojiste la opcion 2')
elif opcion==3:
    mensaje('escojiste la opcion 3.')
else:
    print('error, vuelve a intentarlo.')