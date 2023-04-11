"""
Escribir un programa que pregunte al usuario por el número de horas trabajadas 
y el coste por hora. 
Después debe mostrar por pantalla la paga que le corresponde.
"""

# 1 hora trabajada equivale a 800 pesos
# Primer método
horas_trabajadas = int(input("Colocar las horas trabajadas: "))

coste_por_hora = float(800)
pago = coste_por_hora * horas_trabajadas
print(f"trabajó {horas_trabajadas} horas y le corresponde: {pago} pesos")

# Segundo método
horas = float(input("Introduce tus horas de trabajo: "))
coste = float(input("Introduce lo que cobras por hora: "))
paga = horas * coste
print("Tu paga es", paga)