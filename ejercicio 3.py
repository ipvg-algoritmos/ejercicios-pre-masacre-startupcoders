#Desarrolle un algoritmo que permita ingresar una lista de números y luego muestre el número mayor y el número menor de la lista.
#> **Importante:**
#> - El algoritmo debe permitir al usuario ingresar una cantidad indefinida de números, finalizando la entrada cuando el usuario ingrese un número negativo.

numeros = []  # Inicializa una lista para almacenar los números
while True:  # Bucle infinito para permitir la entrada indefinida de números
    numero = int(input("Ingrese un número (ingrese un número negativo para finalizar): "))  # Solicita al usuario que ingrese un número
    if numero < 0:  # Verifica si el número es negativo
        break  # Sale del bucle si el número es negativo
    numeros.append(numero)  # Agrega el número a la lista   
if numeros:  # Verifica si la lista no está vacía
    numero_mayor = max(numeros)  # Encuentra el número mayor en la lista
    numero_menor = min(numeros)  # Encuentra el número menor en la lista
    print(f"Número mayor: {numero_mayor}")  # Muestra el número mayor
    print(f"Número menor: {numero_menor}")  # Muestra el número menor
else:
    print("No se ingresaron números.")

# Fin del ejercicio, se ha permitido al usuario ingresar una cantidad indefinida de números y se han mostrado el número mayor y el número menor de la lista ingresada.

