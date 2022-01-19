# ESTO ES UN EJERCICIOS DE ADIVINA EL NUMERO
import random

def run():
    numero_random=random.randint(1,100)
    numero_elegido=int(input('Escribe aqui el numero: '))
    while numero_elegido!=numero_random:
        if numero_elegido>numero_random:
            print('Tienes que escojer un numero mas pequeño.')
        else:
            print('Tienes que escojer un numero mayor al proporcionado.')
        numero_elegido=int(input('Elige otro numero: '))
    print("Felicidades Ganaste!!!, Te puedes ir en paz. =)")
if __name__ == '__main__':
    run()