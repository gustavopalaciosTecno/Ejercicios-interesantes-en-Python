"""
Escribir un programa que pregunte al usuario una cantidad a invertir,
el interés anual y el número de años, y 
muestre por pantalla el capital obtenido en la inversión.

"""
# primera alternativa
cantidad_inversion = float(input("Introduce la cantidad a invertir: "))
interes = float(input("coloca el interes anual: "))
year = int(input("Coloca el número de años: "))

calculo = (str(round(cantidad_inversion * (interes / 100 + 1) ** year, 2)))
print(f"total de capital obtenido es: {calculo}")

print("\n")

# segunda alternativa
cantidad = float(input("¿Cantidad a invertir? "))
interes = float(input("¿Interés porcentual anual? "))
años = int(input("¿Años?"))
print("Capital final: " + str(round(cantidad * (interes / 100 + 1) ** años, 2)))