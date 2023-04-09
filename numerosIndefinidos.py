"""
Hacer un scritp que pida números de forma indefinida y 
que pare de ejecutar cuando coloquemos 111

"""
# Primer método
numeros = int(input("Coloca un número: "))
while numeros:
    numeros = int(input("Coloca un número nuevamente: "))
    if numeros == 111:
        break
        
# Segundo método

contador = 1

while contador < 100:
    numero = int(input("Introduce un número: "))    
    
    
    if numero  == 111:
        break
    else:
        print(f"Introduciste el número: {numero}")
        
    
