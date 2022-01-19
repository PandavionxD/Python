// CREACION DEL EJERCICIO QUE ES UNA CALCULADORA SUMA, RESTA, DIVISION, MULTIPLICACION

let num1 = prompt('Escoje el primer numero: ')
let num2 = prompt('Escoje el segundo numero: ')
let res = 0
let operacion=prompt('Escribe aqui entre suma, resta, multi, divi: ')

//Convirtiendo de string a entero
let a= parseInt(num1)
let b = parseInt(num2)


if (operacion=='suma') {
  console.log('el resultado es: ', res=a+b)
}else if (operacion=='resta') {
  console.log('el resultado es: ', res = a-b)
}else if (operacion=='multi') {
  console.log('el resultado es: ', res =a*b)
}else if (operacion == 'divi') {
  console.log('el resultado es: ',res = a/b)
}else {
  console.log('Error al leer el comando ingresado.')
}
