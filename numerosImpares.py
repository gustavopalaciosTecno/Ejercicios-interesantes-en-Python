"""
Hacer un script que muestre todos los números impares que exista 
entre dos números que decida el usuario
"""
"""
# Primer método
numero1 = int(input("Introduce un primer valor numérico: "))
numero2 = int(input("Introduce un segundo valor numérico: "))

for i in range(numero1, numero2):
    if numero1 < numero2:
        if i % 2 == 1:
            print(i)
        
    else:
        print(f"numero {numero1} debe ser menor a numero {numero2}")        
"""    
# Segundo método
numero3 = int(input("Introduce primer valor: "))    
numero4 = int(input("Introduce segundo valor: "))   

for x in range(numero3, (numero4 + 1)):
    if x %2 == 0:
        print(f"{x} ES PAR ")
    else:
        print(f"{x} ES IMPAR ")        