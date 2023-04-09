"""
Realizar un script que me permita extraer el x por ciento de x número.
¿por ejemplo, cuanto es el 20 % de 50?
"""
# Primer método
numero = float(input("Introduzca un valor: "))
porcentaje = float(input("que porcentaje queres saber: "))

resultado = (numero * porcentaje) / 100
print(f"el {porcentaje}% de {numero} es el {resultado}%")


# Segundo método
def calcularPorcentaje():
    numero = float(input("Introduzca un valor: "))
    porcentaje = float(input("que porcentaje queres saber: "))

    resultado = (numero * porcentaje) / 100
    print(f"el {porcentaje}% de {numero} es el {resultado}%")
    
calcularPorcentaje()    
    