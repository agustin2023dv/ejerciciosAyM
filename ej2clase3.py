'''
Escribir un programa que pregunte el nombre del usuario en la consola
y un número entero e imprima por pantalla en líneas distintas el
nombre del usuario tantas veces como el número introducido.
'''

nombre = input("Ingrese su nombre: ")
veces = int(input("Ingrese la cantidad de veces que quiere ver el nombre:"))

i = 0
for i in range(veces):
    print(nombre)
    