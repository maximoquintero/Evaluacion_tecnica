# - Algoritmo para generar contraseñas. (Intermedio).
# • Realizar un algoritmo que permita generar contraseñas aleatorias con los requerimientos 
# proporcionados (longitud mínima de 8 caracteres, al menos una letra mayúscula,
# un carácter especial y un número.)

import random

def generarContraseña():
    letras = ['a','b','c','d','e','f','g','h','i',
              'j','k','l','m','n','ñ','o','p','q',
              'r','s','t','u','v','w','x','y','z']
    
    caracteres = ['!','"','#','$','%','&' ,'/','=','.'
                  '?','¡','°','|','¿','*','{','}','¨',
                  '+','[',']','-','.','_',':',';','>','<']

    contraseña = ''.join(random.sample(letras, 8))
    letra_mayuscula = random.choice(contraseña)
    contraseña = contraseña.replace(letra_mayuscula, letra_mayuscula.upper(), 1)
    contraseña += random.choice(caracteres)

    print(contraseña)

generarContraseña()


