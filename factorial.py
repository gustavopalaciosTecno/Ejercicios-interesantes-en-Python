# Calcular el factorial de un número
# Primer método

def factorial(n):
    if n == 0:
        return 1
    else:
        fact = 1
        for i in range(1, n +1):
            fact = fact * i
        return fact
    
    
print(factorial(10))   

#segundo método

def factorial():
    numero = int(input("coloca un valor numerico para extraer el factorial: "))
    
    if numero == 0:
        return 1
    else:
        fact = 1
        for j in range(1, numero +1):
            fact = fact * j
        return fact
    
print(factorial())                    
    