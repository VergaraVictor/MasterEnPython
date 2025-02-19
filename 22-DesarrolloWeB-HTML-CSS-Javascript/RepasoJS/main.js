// Alertas
// alert('Hola mundo!!');

var nombre = "Víctor Vergara";
var altura = 189;

var concatenacion = nombre + " " + altura;

// var datos = document.getElementById("datos");
// datos.innerHTML = `
//     <h1>Soy la caja de datos</h1>
//     <h2>Mi nombre es: ${nombre}</h2>
//     <h3>Mido: ${altura} cm</h3>
// `;

// // Estructuras de Control
// if(altura >= 190) {
//     datos.innerHTML += '<h1>Eres una persona ALTA</h1>';
// }else{
//     datos.innerHTML += '<h1>Eres una persona BAJITA</h1>';
// }

// // bucle
// for(var i = 2000; i<=2025; i++){
//     // bloque de instrucciones
//     datos.innerHTML += "Estamos en el año: "+i;
// }

function MuestraMiNombre(nombre, altura) {
    var misDatos = `
        <h1>Soy la caja de datos</h1>
        <h2>Mi nombre es: ${nombre}</h2>
        <h3>Mido: ${altura} cm</h3>
    `;

    return misDatos;
}

function imprimir() {
    var datos = document.getElementById("datos");
    datos.innerHTML = MuestraMiNombre("Victor Vergara", 170);
}

imprimir();

var nombres = ['Víctor', 'Antonio', 'Juaquin'];

// alert(nombres[1]);

document.write('<h1>Listado de Nombres</h1>');
/*for(i = 0; i < nombres.length; i++){
    document.write(nombres[i] + '<br/>');
}
Una forma    */
// Otra Forma
nombres.forEach((nombre) => {
    document.write(nombres + '<br/>');
});