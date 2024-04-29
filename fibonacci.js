/*
- Algoritmo de sucesión de Fibonacci. (Avanzado).
• Realiza un algoritmo que dibuje la sucesión de Fibonacci
hasta la posición que el usuario ingrese.
*/

/*
Algoritmo
ingresar cantidad de iteraciones limite
sumar a 0 un 1
agarrar el los ultimos dos numeros y sumarlos
temrinar cuando la cantidad total sea el limite
*/

function fibonacci(num){
    if(num <= 1 || typeof num != 'number'){
        return console.log("Numero no valido")
    }

    let array = [0,1]
    
    for(i = 1; i < num ; i++){
        array.push(array[i] + array[i -1])
    }

    console.log(array)
}

fibonacci(2)