# Veremos las variables locales y globales 
numero=23
text='hola soy una variable global'
def funcion1():
    numero2 = 12
    saludo='soy una variable local'
    print(numero2,saludo)
    print(locals()) #Te va devolver un diccionario con variables locales

funcion1()
print(numero,text)
print(globals()) #Te devuelve las variables globales