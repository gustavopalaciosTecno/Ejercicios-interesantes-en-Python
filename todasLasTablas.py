"""
Mostrar todas las tablas de multiplicar del 2 al 10
"""
# Primer método

def tablas():
    print("######### TABLA DEL 2 #########") 
    for i in range(1,11):
        contador = 2
        print(f"{contador} x {i} = {contador * i}")
    
    print("######### TABLA DEL 3 #########") 
    for i in range(1,11):
        contador = 3
        print(f"{contador} x {i} = {contador * i}")
        
    print("######### TABLA DEL 4 #########")     

    for i in range(1,11):
        contador = 3
        print(f"{contador} x {i} = {contador * i}")   
        
    print("######### TABLA DEL 5 #########")    
    
    for i in range(1,11):
        contador = 5
        print(f"{contador} x {i} = {contador * i}")    
        
    print("######### TABLA DEL 6 #########")    
    
    for i in range(1,11):
        contador = 6
        print(f"{contador} x {i} = {contador * i}") 
        
    print("######### TABLA DEL 7 #########")    
    
    for i in range(1,11):
        contador = 7
        print(f"{contador} x {i} = {contador * i}")
        
    print("######### TABLA DEL 8 #########")    
    
    for i in range(1,11):
        contador = 8
        print(f"{contador} x {i} = {contador * i}")   
        
    print("######### TABLA DEL 9 #########")    
    
    for i in range(1,11):
        contador = 9
        print(f"{contador} x {i} = {contador * i}")    
        
        
    print("######### TABLA DEL 10 #########")    
    
    for i in range(1,11):
        contador = 10
        print(f"{contador} x {i} = {contador * i}")                
                                 

tablas() 
      
# Segundo método

for cabecera in range(2, 11):
    print("#################")
    print(f"TABLA DEL {cabecera}")
    print("#################")
    
    for i in range(1,11):
        print(f"{cabecera} x {i} = {cabecera * i}")
        
print("\n")  

"""
Proba las dos o elegir una.

"""          