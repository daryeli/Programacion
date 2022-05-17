#5.4 Desarrolle una función que acepte una variable string como primer parámetro y la cantidad de carácteres como segundo parámetro
#La función debe retornar un nuevo string que consista en el string original y el número correcto de caráteres necesario para que el string se salga centrado.

import os

Nombre = ("Daryeli")
Caractéres = len(Nombre)

def Centrado (Nombre, Caractéres):
    size = os.get_terminal_size().columns - Caractéres;
    print (Nombre.center(size))
    print ("Los caractéres que necesitamos para centrarse son:", size)

Centrado (Nombre, Caractéres)