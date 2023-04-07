"""
Crear un script que muestre todos los valores entre dos números
que diga el usuario
"""
valor1 = int(input("Introduce primer valor: "))
valor2 = int(input("Introduce segundo valor: "))
if valor1 < valor2:
    for i in range(valor1, valor2 + 1):
        print(i) 
else:
    print(f"no se puede realizar la operacion porque {valor2} es menor que {valor1}")


