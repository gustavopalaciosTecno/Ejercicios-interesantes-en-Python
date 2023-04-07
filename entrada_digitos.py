"""
Crear un programa que determine por teclado si un valor es string, booleano,
entero o flotante.
"""

entrada = input("Introduce un valor: ")

if entrada.isdigit():
    print("El dato es un entero")
elif entrada.replace(".", "").isdigit():
    print("el dato ingresado es un flotante")  
elif entrada == "True" or entrada == "False":
    print("El valor es un booleano")      
else:
    print("el dato ingresado es un string")    


