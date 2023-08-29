'''
Escribir un programa que pregunte una fecha en formato dd/mm/aaaa
y muestre por pantalla la misma fecha en formato dd de <mes> de
aaaa donde <mes> es el nombre del mes.

La respuesta debe ser similar a:

23 de octubre de 2018

PD: Pueden usar la función split para dividir la fecha en subcadenas
'''

import datetime
import locale

# Configurar la configuración regional para español
locale.setlocale(locale.LC_TIME, 'es_ES') 

# Obtener la fecha del usuario en formato dd/mm/aaaa
fecha_str = input("Ingrese una fecha en formato dd/mm/aaaa: ")

# Dividir la fecha en subcadenas
dia, mes, anio = fecha_str.split('/')

# Convertir las subcadenas a valores numéricos
dia = int(dia)
mes = int(mes)
anio = int(anio)

# Obtener el nombre del mes
nombre_mes = datetime.date(anio, mes, dia).strftime('%B')


fecha_formateada = f"{dia} de {nombre_mes} de {anio}"
print(fecha_formateada)
