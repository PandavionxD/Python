const persona={
  nombre : 'Alex',
  apellido : 'Artica',
  edad:28,
  info: function(){
    console.log(`Tu nombre es ${this.nombre},
el apellido es ${this.apellido},
y tu edad es ${this.edad}`)
  }
}
persona1 = persona.info()
