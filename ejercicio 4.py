#Cree un algoritmo que solicite al usuario ingresar una lista de números y luego calcule el promedio de los números ingresados.
#Importante
#El algoritmo debe permitir al usuario ingresar una cantidad indefinida de números, finalizando la entrada cuando el usuario ingrese un número negativo.

lista_numeros = []  # Inicializa una lista vacía para almacenar los números
while True:  # Bucle infinito para permitir la entrada indefinida de números
    numero = int(input("Ingrese un número (negativo para finalizar): "))  # Solicita al usuario que ingrese un número
    
    if numero < 0:  # Verifica si el número es negativo
        break  # Sale del bucle si el número es negativo
    
    lista_numeros.append(numero)  # Agrega el número a la lista     
if lista_numeros:  # Verifica si la lista no está vacía
    promedio = sum(lista_numeros) / len(lista_numeros)  # Calcula el promedio de los números en la lista
    print(f"El promedio de los números ingresados es: {promedio:.2f}")  # Muestra el promedio con dos decimales 

else:
    print("No se ingresaron números.")  # Mensaje si la lista está vacía    
# Fin del ejercicio, se ha calculado el promedio de los números ingresados por el usuario

