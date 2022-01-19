nombre= prompt('Cual es tu nombre: ')
edad =  prompt('Cual es tu edad: ')

// FUNCION
// function persona(nombre,edad){
//   return `Hola tu nombre es ${nombre}
//   y tu edad es ${edad}, Feliz Cumpleaños!`
// }


// FUNCION FLECHA
const persona = (nombre,edad)=>{
    return `Hola tu nombre es ${nombre}
    y tu edad es ${edad}, Feliz Cumpleaños!`
}


// LLAMAMOS LA FUNCION FLECHA CREADA
let persona1 = persona(nombre,edad)
console.log(persona1)
