# Definimos la clase Persona
class Persona():
    texto = ''
    def __init__(self,nombre,apellido,edad):
        self.nombre = nombre
        self.apellido = apellido
        self.edad = edad
    def saludar(self):
        self.texto = f'Hola, tu nombre es: {self.nombre} {self.apellido} y tu edad es -> {self.edad}'
        return self.texto
    def __str__(self) -> str:
        return f"Hola que tal soy la clase Padre...!"



# Se crea la instancia de la clase
persona1 = Persona('Alex','Artica',24)
print(persona1.nombre)
print(persona1.apellido)
print(persona1.edad)
texto = persona1.saludar()
print(texto)

# Herencia
class Adulto(Persona):
    def __init__(self, nombre, apellido, edad,deporte):
        super().__init__(nombre, apellido, edad)
        self.deporte=deporte
    def saludar(self):
        return super().saludar() + ' donde el deporte que practicas es '+self.deporte
    def grabarTarjeta(self,tarjeta):
        self.tarjeta = tarjeta
        return self.tarjeta
    def __str__(self) -> str:
        return super().__str__() + f", desde la clase padre yo soy una clase hijo Adulto"

adulto1 = Adulto('Juan','Rojas',25,'Futbol')
print(adulto1.nombre)
print(adulto1.apellido)
print(adulto1.edad)
print(adulto1.deporte)
print(adulto1)
print(adulto1.saludar())
adulto1.grabarTarjeta(123456)
print(adulto1.tarjeta)

print(persona1)
print(adulto1)