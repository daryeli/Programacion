#5.1 Defina una función en Python que acepte el radio y devuelva el valor del area de un circulo de esas dimensiones

import math

print("El valor da la radio:", 2)
pi = math.pi
print("El valor de pi es:", pi)

r = 2 #capturando la radio.
a = math.pi * math.pow(r, 2)
print("El area del circulo con radio", r, "es:", round(a, 2))

def saludarProfesor (nombre):
    print("Saludos profesor", nombre)
    print("Aqui el resultado de el area de un circulo con radio 2")
    print("El resultado del area nos da 12.57")

nombre = "Carlos Batalla"
saludarProfesor(nombre)