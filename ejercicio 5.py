#Desarrolle un programa que permita ingresar una matriz de números enteros de 3x3. Luego, el programa debe recorrer la matriz y contar cuántos números son positivos, negativos y ceros. Además, debe indicar si la suma de los elementos de la diagonal principal es mayor, menor o igual a la suma de la diagonal secundaria.

#> **Importante:**
#> - Debe utilizar ciclos para recorrer la matriz.
#> - Utilice operadores lógicos y condicionales anidadas (al menos un `elif`).
#> - Al final, muestre la cantidad de positivos, negativos y ceros, y el resultado de la comparación entre las diagonales.

matriz = []  # Inicializa una lista para almacenar la matriz
for i in range(3):  # Bucle para las filas de la matriz
    fila = []  # Inicializa una lista para      
    for j in range(3):  # Bucle para las columnas de la matriz
        numero = int(input(f"Ingrese el número para la posición ({i+1}, {j+1}): "))  # Solicita al usuario que ingrese un número
        fila.append(numero)  # Agrega el número a la fila   
    matriz.append(fila)  # Agrega la fila a la matriz
positivos, negativos, ceros = 0, 0, 0  # Inicializa contadores para positivos, negativos y ceros
suma_diagonal_principal = 0  # Inicializa la suma de la diagonal principal      
suma_diagonal_secundaria = 0  # Inicializa la suma de la diagonal secundaria
for i in range(3):  # Bucle para recorrer las filas de la matriz
    for j in range(3):  # Bucle para recorrer las columnas de la matriz
        numero = matriz[i][j]  # Obtiene el número en la posición (i, j)
        
        if numero > 0:  # Verifica si el número es positivo
            positivos += 1  # Incrementa el contador de positivos
        elif numero < 0:  # Verifica si el número es negativo
            negativos += 1  # Incrementa el contador de negativos
        else:  # Si no es ni positivo ni negativo, debe ser cero
            ceros += 1  # Incrementa el contador de ceros
        
        if i == j:  # Verifica si estamos en la diagonal principal
            suma_diagonal_principal += numero  # Suma el número a la diagonal principal
        if i + j == 2:  # Verifica si estamos en la diagonal secundaria
            suma_diagonal_secundaria += numero  # Suma el número a la diagonal secundaria
# Muestra los resultados
print(f"Números positivos: {positivos}")  # Muestra la cantidad de números positivos
print(f"Números negativos: {negativos}")  # Muestra la cantidad de números negativos
print(f"Números ceros: {ceros}")  # Muestra la cantidad de ceros    
# Compara las sumas de las diagonales
print(f"Suma de la diagonal principal: {suma_diagonal_principal}")  # Muestra la suma de la diagonal principal              
if suma_diagonal_principal > suma_diagonal_secundaria:  # Compara las sumas de las diagonales
    print("La suma de la diagonal principal es mayor que la de la diagonal secundaria.")  # Mensaje si la diagonal principal es mayor
elif suma_diagonal_principal < suma_diagonal_secundaria:  # Compara las sumas de las diagonales
    print("La suma de la diagonal principal es menor que la de la diagonal secundaria.")  # Mensaje si la diagonal principal es menor
else: # Si las sumas son iguales
    print("La suma de la diagonal principal es igual a la de la diagonal secundaria.")
# Fin del ejercicio, se ha contado la cantidad de números positivos, negativos y ceros, y se ha comparado la suma de las diagonales de la matriz ingresada por el usuario

