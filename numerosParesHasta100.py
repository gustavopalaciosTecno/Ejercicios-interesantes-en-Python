"""
Crear un script que nos muestre todos los números pares del 1 hasta el 100
"""
"""
# Primer método
for i in range(1, 101):
    if i % 2 == 0:
        print(i)
"""        
        
# Segundo método
def pares():
    valor = int(input("coloca un valor dentro del rango de 1 a 100: "))
    if valor %2 == 0 and valor > 1 and valor <=100:
        for i in range(1,valor + 1):
            if i %2 == 0:
                print(f"es numero par: {i}")
    else:
        print("solo se aceptan numeros pares")       
    return (valor)            
            
    
                          
            
pares()    
            