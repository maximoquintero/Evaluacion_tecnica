# - Algoritmo de un ahorcado. (Intermedio).
# • Se genera una palabra aleatoria (oculta al usuario) y el usuario
# debe ingresar letra por letra para intentar adivinar la palabra,
# se debe validar que las letras coincidan con la posición de las letras de la 
# palabra generada. Máximo 5 errores.

import random

palabras = ['Camello','Lobo','Topo','Rana','Canguro',
            'Hámster','Conejo','Asno','Lagartija',
            'Becerro','Alacrán','Mandril','Armadillo',
            'Caimán','Oso']

palabra = random.choice(palabras).lower()

vidas = 5

print("Bienvenido, vamos a jugar al ahorcado tienes 5 vidas")
print("Aqui va la palabra, es un animal")

letras = []

while vidas > 0:

    for letra in palabra:
        if letra in letras:
            print(letra, end=' ')
        else:
            print("*", end=' ')
    print()
    
    intento = input("Dame una letra o la palabra completa: ").lower()
    
    if len(intento) > 1:
        if intento == palabra:
            print("Ganaste =)")
            break
        else:
            vidas -= 1
            print("No era ese y perdiste una vida. Te quedan: ", vidas)
            if vidas == 0:
                print("Has perdido =(")
                break
    elif len(intento) == 1:
        if intento in palabra:
            letras.append(intento)
            print("¡Si esta la letra!")
        else:
            vidas -= 1
            print("No esta la letra, perdiste una vida. Te quedan: ", vidas)
            if vidas == 0:
                print("Has perdido =(")
                break
    else:
        print("Por favor, ingresa una letra o la palabra completa.")