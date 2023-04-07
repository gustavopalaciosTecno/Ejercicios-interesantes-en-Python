""""
Realizar un programa que por medio del tecaldo me permite extraer la tabla de mutiplicar
del valor que ingrese.

"""
print("#### TABLA  DE MUTIPLICAR ######")
valor = int(input("Ingresar un valor numérico para crear tabla: "))

for i in range(0,11):
    print(f" {valor}x{i} = {valor * i}")

print(f"Tabla de mutiplicar del: {valor}")