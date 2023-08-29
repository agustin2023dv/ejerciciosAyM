'''
Dada la siguiente lista

numeros = [3, 5, 2, 8, 6]

Obtén el número mayor
'''

numeros = [3, 5, 2, 8, 6]
mayor= 0
for i in numeros:
    if i>mayor:
        mayor = i

print(mayor)