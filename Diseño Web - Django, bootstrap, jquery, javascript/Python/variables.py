numero = 12
cadena = 'hola'
numeroDecimal = 12.23
flotante = True

print(type(numero))
print(type(cadena))
print(type(numeroDecimal))
print(type(True))

num1 = 12 
num2 = 13

print(f'la suma de estos numeros {num1} y {num2} es {num1+num2}')


# Metodos de cadenas
cadenaTexto= 'Hola mundo, te saludo desde Python ;)'
# Contar cuantos valores hay en la cadena
print(cadenaTexto.count('e'))
# find e index retorna la ubicacion desde cero
# find si no encuentra el valor retorna -1, index si no encuentra el valor retorna error
print(cadenaTexto.find('Python'))
print(cadenaTexto.index('Python'))
# rindex, rfind buscan cadenas pero en orden inverso no desde cero
print(cadenaTexto.rindex('o'))
#startswith, endswith consultan si empieza por una cadena en especifico o o finaliza
print(cadenaTexto.startswith('Hola'))
#los metodos is... retornan valores booleanos

#capitalize -> capitaliza el texto
#encode -> cadenaTexto.encode('utf-8)
#center, ljust , rjust -> cadenaTexto.center(10,'-')
print(cadenaTexto.center(80,'*'))
#lower y uppercase -> son para minusculas y mayusculas
#swapcase -> cambia las minusculas a mayusculas y viceversa
#strip,lstrip, rstrip -> elimina los espacio antes y despues de la cadena
cadena3 = ' hola mundo '
print(cadena3.strip())

#replace ->r
# reemplaza una cadena por otra
print(cadena3.replace('mundo','Python'))

#Split -> separa la cadena en string a lista
cadena4= 'Hola mundo, desde Python! ;)'
print(cadena4.split(" "))

#Separar cadenas de lineas
cadena5 = """
hola te saludo desde
Python!!
mi alias,
PandavionxD
"""
print(cadena5.splitlines())

#rpartition -> hace lo mismo que split pero de busqueda inversa

#metodo join
frases = ['Buen','día','me','llamo','Alex']
frase = " ".join(frases)
print(frase)
print(type(frase))