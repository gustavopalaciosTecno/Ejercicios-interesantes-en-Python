"""
Crear un script que pida por pantalla dos valores y realice
todas las operaciones básicas de una calculadora.
"""
# Primer método
def calculadora():
    valor1 = int(input("Introduce primer valor: "))
    valor2 = int(input("Introduce segundo  valor: "))
    suma = valor1 + valor2
    resta = valor1 - valor2
    division = valor1 / valor2
    multiplicacion = valor1 * valor2
    print(f"el resultado de la suma es: {suma}")
    print(f"el resultado de la resta es: {resta}")
    print(f"el resultado de la division es: {division}")
    print(f"el resultado de la multiplicacion es: {multiplicacion}")
    
    
calculadora()    

# Segundo método
valor2 = int(input("Introduce primer valor: "))
valor3 = int(input("Introduce segundo  valor: "))
print("el resultado de la suma es: " + str(valor2 + valor3))
print("el resultado de la resta es: " + str(valor2 - valor3))
print("el resultado del cociente es: " + str(valor2 / valor3))
print("el resultado del producto es: " + str(valor2 * valor3))