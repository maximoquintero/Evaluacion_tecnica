/*
- Algoritmo para validar palíndromos. (Básico). 
• Realizar un sencillo algoritmo para validar si una palabra es un palíndromo,
el usuario debe ingresar una palabra y se le retorna un mensaje de valido o invalido.
Un palíndromo es una palabra o frase que se lee igual en un sentido que en otro. 
*/

function verificarPalindromo(palabra){
    if(typeof palabra != "string"){
        return console.log("Palabra no valida")
    }

    let alReves = '';
    for(let i = palabra.length - 1; i >= 0 ;i--){
        alReves += palabra[i];
    }
    let resultado = alReves == palabra ? 'valido':'invalido';
    console.log(resultado);
}

verificarPalindromo("reconocer")
