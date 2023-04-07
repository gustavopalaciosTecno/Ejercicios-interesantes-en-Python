#realizar un programa que pida por consola números y nos diga si son pares o impares

# primer método
"""  
try:
    entrada = int(input("Ingresar un valor numérico: "))

    if entrada %2 == 0:
        print(f"el valor {entrada} es par")
    elif entrada %2 == 1:
        print(f'el valor {entrada} es impar')
except Exception as e:        
        print('introduce valores numéricos solamente', e)        
"""    
# segundo método
while True:
    num = input("Ingresa un número (o 'salir' para terminar): ")
    if num.lower() == 'salir':
        break
    try:
        num = int(num)
        if num % 2 == 0:
            print(num, "es un número par")
        else:
            print(num, "es un número impar")
    except ValueError:
        print("Ingresa un número válido")
  