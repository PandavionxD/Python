// AQUI CREAREMOS UNA LISTA EN JAVASCIPT
let nombres = [
  'alex',
  'daniel',
  'pedro',
  'juan'
]
console.log(nombres)

// UNA FORMA DE ITERAR LOS ELEMENTOS DEL ARRAY
// for (let nombre of nombres) {
//     console.log(nombre)
// }

// OTRA FORMA DE ITERAR LOS ELEMENTOS DEL ARRAY
for (let i = 0; i < nombres.length; i++) {
   console.log(nombres[i])
}

// METODOS DE ARRAYS
nombres.pop()    //Eliminando un elemento del array
nombres.push('carlos')  //Añadiendo un elemento del array
console.log(nombres)

//UNION DE ARRAYS
let frutas = ['uva','manzana','fresa','pera']

let arrayCompleto = [...nombres,...frutas]
console.log(arrayCompleto)
console.log(arrayCompleto.length)

//MATRICES
let matriz = [ [1,2,3],[4,5,6],[7,8,9]]
console.log(matriz[0])
console.log(matriz[0][2])
