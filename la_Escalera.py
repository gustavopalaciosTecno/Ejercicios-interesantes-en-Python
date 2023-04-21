"""
* Crea una función que dibuje una escalera según su número de escalones.
 * - Si el número es positivo, será ascendente de izquiera a derecha.
 * - Si el número es negativo, será descendente de izquiera a derecha.
 * - Si el número es cero, se dibujarán dos guiones bajos (__).
 * 
 * Ejemplo: 4
 *         _
 *       _|       
 *     _|
 *   _|
 * _|
 * 
 */
 
 """
 
valor = int(input("coloca un valor numérico: "))


if valor == 0:
    print("__") 
elif valor > 0:
    for i in range (0,valor):
        print("*"*i)
else:
    for i in range(valor, 0):
        print("*"*abs(i))            
   
    
        
 