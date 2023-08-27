'''
Una juguetería tiene mucho éxito en dos de sus productos: payasos y
muñecas. 
Suele hacer venta por correo y la empresa de logística les
cobra por peso de cada paquete así que deben calcular el peso de los
payasos y muñecas que saldrán en cada paquete a demanda. 

Cada payaso pesa 112 g y cada muñeca 75 g. 

Escribir un programa que lea el
número de payasos y muñecas vendidos en el último pedido y calcule
el peso total del paquete que será enviado.

PD: Debe resolverse haciendo uso de funciones
'''
last_order = {'Clowns': 10, 'Dolls': 25}

def calculate_weight(clowns, dolls):
    clowns = clowns * 112
    dolls = dolls * 75
    total_weight = clowns + dolls
    return total_weight

last_order_weight = calculate_weight(last_order['Clowns'], last_order['Dolls'])
print(f"El peso total del pedido es de {last_order_weight} kgs")

