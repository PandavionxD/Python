import random

def generar_contraseña():
    mayuscula =['A','B','C','D','E','F','G']
    minuscula = ['a','b','c','d','e','f','g']
    caracteres_especiales = ['-',',','.','-','@']
    numeros=['1','2','3','4','5','6','7','8','9','0']
    caracteres = minuscula+mayuscula+caracteres_especiales+numeros
    contraseña = []
    for i in range(15):
        caracteres_random= random.choice(caracteres)
        contraseña.append(caracteres_random)
    contrasena = ''.join(contraseña)
    return contrasena

def run():
    contrasena= generar_contraseña()
    print('La contraseña es: ', contrasena)

if __name__ == '__main__':
    run()