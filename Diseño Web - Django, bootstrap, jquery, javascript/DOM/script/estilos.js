// Seleccionamos los elementos de titulo y parrafos para cambiarlos de color
let titulo = document.querySelector('h1')
let parrafo = document.querySelector('p')

// Cambiamos los colores de los elementos seleccionados

titulo.style.color = 'green'
parrafo.style.color = 'pink'
parrafo.style.fontSize = '20px'

let parrafo1 = document.querySelector('.p1')
let parrafo2 = document.querySelector('.p2')

parrafo1.textContent = 'hola mundo desde JavaScript'
parrafo2.innerHTML = `
<h3> Esto es un texto desde JavaScript</h3>
<p> me llamo alex y estamos jugando en <b> javaScript </b></p>
`
