#5.2 Defina una función en python que acepte 3 valores y devuelva solo el maximo de los tres

Valor1 = float(input("Ingrese el primer valor:"))
Valor2 = float(input("Ingrese el segundo valor:"))
Valor3 = float(input("Ingrese el tercer valor:"))

if Valor2 < Valor1 > Valor3:
    print("El valor mayor es el número:", Valor1)
elif Valor1 < Valor2 > Valor3:
    print("El valor mayor es el número:", Valor2)
elif Valor1 < Valor3 > Valor2:
    print("El valor mayor es el número:", Valor3)
else:
    print("Todos los valores son iguales")

def BuenasTardes (profesor):
    print("Buenas tardes profesor", (profesor))
    print("Segundo ejercicio sobre aceptar valores y devolver el maximo")
    print("El valor máximo de los tres es:", Valor2 < Valor1 > Valor3)
    print("El valor máximo de los tres es:", Valor1 < Valor2 > Valor3)
    print("El valor máximo de los tres es:", Valor1 < Valor3 > Valor2)

profesor = "Carlos Batalla"
BuenasTardes(profesor)