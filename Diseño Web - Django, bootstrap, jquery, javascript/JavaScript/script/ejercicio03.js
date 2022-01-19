//Ejercicio03 creando un emdia aritmetica con una funcion:

let a = prompt('Introduce aqui el primer numero: ')
let b = prompt('Introduce el segundo numero: ')
let c = prompt('Introduce un tercero numero: ')

let num1 = parseInt(a)
let num2 = parseInt(b)
let num3 = parseInt(c)

const suma =(a,b,c)=>{
    return (a+b+c)/3
}
let suma1=suma(num1,num2,num3)

console.log('la media aritmetica es: '+suma1)
