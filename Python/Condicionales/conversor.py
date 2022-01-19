# CREANDO CONVERSOR DE SOLES A DOLARES.
# USAREMOS NUESTRA APP PARA DARLE MAS SENTIDO
def conversor(moneda,tipomoneda,cambio):
    moneda = float(input("Cuantos " + tipomoneda+ " quieres convertir a dolares: "))
    dolar = round(moneda/cambio,2)
    print('Los dolares son: ',dolar)

print('''
Bienvenidos a nuestro conversor de Monedas :)
Tienes que escojer una de las 3 opciones a continuacion
1.De soles a Dolar
2.De pesos a Dolar
3.De Euros a Dolar
''')
opcion = int(input("Escribe aqui la opcion.: "))
if opcion==1:
    conversor(1,'soles',3.1416)
elif opcion==2:
    #ESTO ES UN EJEMPLO DESARROLLA LOS OTROS 3 CASOS
    pass
elif opcion==3:
    pass
else:
    print("Error no escojiste la opcion correcta.")




