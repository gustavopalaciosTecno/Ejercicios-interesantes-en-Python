"""
Escribir un programa que lea un entero positivo, 
introducido por el usuario y después muestre en pantalla la suma de todos los enteros 
desde 1 hasta n .La suma de los n primeros enteros positivos 
puede ser calculada de la siguiente forma:

"""
# Primer método
numero = int(input("Coloca un número: "))

if numero != 0:
    
    resultado = numero * (numero + 1) / 2
    print(resultado)
else:
    print("debes colocar un número mayor a cero (0)")    



# Segundo método
n = int(input("Introduce un número entero: "))
suma = n * (n + 1) / 2
print("La suma de los primeros números enteros desde 1 hasta " + str(n) + " es " + str(suma))