alert('En esta pagina mencionaremos unos ejemplos de Objetos')
const personas = {
  persona1 :'Alex',
  persona2:'Daniel',
  persona3:'Juan',
  persona4:'Carlos'
}
console.log(personas)

//ITERAR LOS ELEMENTOS DE UN OBJETO

for (let persona in personas) {
  console.log(personas.persona1)
}

for (let persona1 in personas) {
  console.log(personas[persona1])
  console.log(persona1)
}

//CREANDO OTRO OBJETO CON PARAMETRO ADENTRO
const numeros = {
  one:1,
  two:2,
  three:3,
  four:4,
  five:5,
  metodo:function(){
    alert('el numero uno es '+this.one)
  }
}
console.log(numeros.metodo())
