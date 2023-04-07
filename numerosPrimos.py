# Crear un programa que extraiga los números primos

# primer método
def encontrar_primos(valor):
    # Crear una lista con todos los números del 2 hasta el valor
    numeros = list(range(2, valor+1))
    # Inicializar una lista vacía para los números primos
    primos = []
    # Iterar sobre la lista de números
    while numeros:
        # El primer número de la lista es un primo
        primo = numeros.pop(0)
        primos.append(primo)
        # Eliminar los múltiplos del primo de la lista
        numeros = [n for n in numeros if n % primo != 0]
    return primos


print(encontrar_primos(2))
print(encontrar_primos(3))
print(encontrar_primos(4))
print(encontrar_primos(5))
print(encontrar_primos(6))
print(encontrar_primos(7))
print(encontrar_primos(8))
print(encontrar_primos(9))
print(encontrar_primos(10))

# Segundo método
def encontrar_primos2():
    # Solicitar al usuario que ingrese un valor
    valor = int(input("Ingrese un valor: "))
    # Crear una lista con todos los números del 2 hasta el valor
    numeros = list(range(2, valor+1))
    # Inicializar una lista vacía para los números primos
    primos = []
    # Iterar sobre la lista de números
    while numeros:
        # El primer número de la lista es un primo
        primo = numeros.pop(0)
        primos.append(primo)
        # Eliminar los múltiplos del primo de la lista
        numeros = [n for n in numeros if n % primo != 0]
    return primos

print(encontrar_primos2())