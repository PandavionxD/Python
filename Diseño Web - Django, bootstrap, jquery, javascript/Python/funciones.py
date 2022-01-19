# Aqui vamos a declarar funciones 
res =None
def run():
    num1 = int(input('Escribe aqui el primer numero: '))
    num2 = int(input('Escribe aqui el segundo numero: '))
    suma(num1,num2)

def suma(num1,num2):
    """
    ESTO ES COMO GENERAR UNA DESCRIPCION DENTRO DE UNA FUNCION EN PYTHON----->
    esto es la funcion suma
    consiste en suma dos valores cuando llames la funcion
    retornara una suma de dos variables
    """
    res = num1+num2
    print(f'La suma es {res}')

if __name__ == '__main__':
    run()