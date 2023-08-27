## Escribir un programa que pregunte al usuario por el número de horas trabajadas y el coste por hora. 
## Después debe mostrar por pantalla la paga que le corresponde.

# Pedir al usuario el número de horas trabajadas y el coste por hora
horas_trabajadas = float(input("Ingrese el número de horas trabajadas: "))
coste_por_hora = float(input("Ingrese el coste por hora: "))

# Calcular pago total
paga = horas_trabajadas * coste_por_hora

# Mostrar la paga que le corresponde al usuario
print("La paga correspondiente es:", paga)

