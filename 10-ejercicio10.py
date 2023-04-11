"""
Una juguetería tiene mucho éxito en dos de sus productos: payasos y muñecas. 
Suele hacer venta por correo y la empresa de logística les cobra por peso de cada paquete 
así que deben calcular el peso de los payasos y muñecas que saldrán en cada paquete a demanda. 
Cada payaso pesa 112 g y cada muñeca 75 g. 
Escribir un programa que lea el número de payasos y muñecas vendidos 
en el último pedido y calcule el peso total del paquete que será enviado.

"""
# la primera la hice je moi
juguete_payaso = 112
juguete_munieca = 75

vender_juguete_payaso = int(input("Coloca la cantidad de jueguetes payasos a vender: "))
vender_juguete_munieca = int(input("Coloca la cantidad de jueguetes muñeca a vender: "))

calculo_peso1 = juguete_payaso * vender_juguete_payaso
calculo_peso2 = juguete_munieca * vender_juguete_munieca
total = calculo_peso1 + calculo_peso2
print(f"el peso total del pauete es de {total} gramos")
print("\n")
# la segunda the solution
peso_payaso = 112
peso_muñeca = 75
payasos = int(input("Introduce el número de payasos a enviar: "))
muñecas = int(input("Introduce el número de muñecas a enviar: "))
peso_total = peso_payaso * payasos + peso_muñeca * muñecas
print("El peso total del paquete es " + str(peso_total))