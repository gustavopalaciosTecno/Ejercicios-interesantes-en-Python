"""
Escribir un programa que muestre los cuadrados de los 
60 primeros números naturales
"""
# Primer método

for j in range(1,61):
    print(f"el cuadrado de {j} es {j * j}")


# Segundo método
contador = 0

while contador <= 60:
    cuadrado = contador * contador
    print(f"el valor de {contador} es {cuadrado}")
    
    contador+=1
    
"""
Ejecutar el primer método o el segundo. si ejecute el primero, comento el segundo fragmento 
de codigo y si ejecuto el segundo, 
comento el primer fragmento de código.
esto es así para ver en más detalles los resultados.
"""    