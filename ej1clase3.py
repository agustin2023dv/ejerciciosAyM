'''
Haz un pequeño programa que:

1- Pida por consola el nombre, apellido y género

2-Crea un diccionario con la información de la persona

3-Muestra por pantalla con los datos de la persona, concatenando los
datos de manera legible.

Ej: print(f"La marca es: {auto[‘marca’]}.")
'''

nombre = input("Por favor, ingresa tu nombre: ")
apellido = input("Por favor, ingresa tu apellido: ")
genero = input("Por favor indica tu genero: ")


diccionario_persona = {'Nombre': nombre,
                        'Apellido':apellido,
                        'Genero':genero}

print('Nombre:'+diccionario_persona['Nombre']+'\nApellido:'+diccionario_persona['Apellido']
        +'\nGenero:'+diccionario_persona['Genero'])