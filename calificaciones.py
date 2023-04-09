"""
Hacer un script que pida la nota de 15 alumnos y
sacar por pantalla cuantos aprobaron y cuantos desaprobaron.
"""


contador = 1
aprobados = 0
desaprobados = 0

numeros_alumnos = int(input("Cuantos alumnos tenés: "))

while contador <= numeros_alumnos :
    nota = int(input(f"¿Qué nota queres ponerle al \"alumno {contador}\"? "))
    
    
    if nota >=6:
        aprobados+=1
    else:
        desaprobados += 1
                
    
    contador+=1
    
    
print(f"Total alumnos aprobados: {aprobados}")    
print(f"Total alumnos desaprobados: {desaprobados}")  

        

