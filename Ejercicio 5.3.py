#5.3 Dado una lista de enteros, defina una función en python que devuelva la suma de solo los valores impares de dicha lista

vLista = [1, 5, 8, 7, 2, 13, 16, 4, 25, 29, 18, 31, 40, 55, 36]

def SumarLista (vLista):
    suma = 0 

    for n in vLista: 
        if n % 2 != 0:
            suma = suma + n
    
    return suma

resultado = SumarLista (vLista)

print("Dada la lista:", (vLista))
print("La suma de los números impares es:", resultado)