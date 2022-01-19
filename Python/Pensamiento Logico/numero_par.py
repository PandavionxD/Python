#Creamos nuestro programa para numeros pares
def is_par(numero):
    if numero%2==0:
        return True

def run():
    num_1=int(input("Escribe aqui el numero: "))
    if is_par(num_1):
        print('El numero es par')
    else:
        print('El numero no es par')


if __name__ == '__main__':
    run()