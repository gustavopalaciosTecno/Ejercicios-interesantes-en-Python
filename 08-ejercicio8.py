"""
Escribir un programa que pida al usuario dos números enteros 
y muestre por pantalla la <n> entre <m> da un cociente <c> y un resto <r> 
donde <n> y <m> son los números introducidos por el usuario, 
y <c> y <r> son el cociente y el resto de la división entera respectivamente.
"""
# mejor alternativa:
n = input("Introduce el dividendo (entero): ")
m = input("Introduce el divisor (entero): ")
print(n + " entre " +  m + " da un cociente " + str(int(n) // int(m)) + " y un resto " + str(int(n) % int(m)))





# otra alternativa
n = int(input("Coloca un primer valor numérico: "))
m = int(input("Coloca un segundo valor numérico: "))

print(f"el número que elegiste es el {n} y el {m} para la operación")
print("\n")
primer_resulado = n // m
segundo_resultado = n % m
print(f"el resultado del cociente entre {n} y {m} es: {primer_resulado}")
print(" ")
print(f"el resto entre {n} y {m} es el {segundo_resultado}")
