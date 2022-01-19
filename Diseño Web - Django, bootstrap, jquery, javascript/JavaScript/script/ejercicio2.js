//Ejercicio de numeros pares
let limite = prompt('escribe aqui el numero limite  para el conteo: ')
let contador = parseInt(limite)
let listas = []
while (contador>0 ) {
    if (contador%2==0){
      listas.push(contador)
    }
    contador-=1
    }
for (let lista of listas) {
  alert(lista)
console.log('la longitud de la lista es '+listas.length)}
