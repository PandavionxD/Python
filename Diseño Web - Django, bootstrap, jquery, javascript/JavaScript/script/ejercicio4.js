const media = (numeros)=>{
  res = 0
  for (let numero of numeros) {
    res +=numero
  }
  let longitud=numeros.length
  let media = res / longitud

  return media
}
lista = [1,2,3]
let numeros1 =media(lista)
console.log('la media de los items de la lista son: ',numeros1)
