'''
Implementa una función que te cree un arreglo con los siguientes
parámetros:

n=el tamaño del arreglo

m=múltiplos que contendrá el arreglo
'''

def crear_arreglo(tamanio,multiplo):
    arreglo = []
    for i in range(tamanio):
        if i % multiplo == 0:
            arreglo.append(i)
    return arreglo

print(crear_arreglo(6,3))