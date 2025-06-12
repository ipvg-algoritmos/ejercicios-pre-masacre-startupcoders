#Cree un programa que reciba una cadena de texto e indique cuántas vocales y cuántas consonantes contiene.

#> **Importante:**
#> - El programa debe considerar tanto mayúsculas como minúsculas.
#> - Las letras acentuadas y la "ñ" deben ser consideradas como consonantes.

cadena = input("Ingrese una cadena de texto: ")  # Solicita al usuario que ingrese una cadena de texto
vocales = "aeiouAEIOU"  # Define las vocales en mayúsculas y minúsculas 
consonantes = "bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ"  # Define las consonantes en mayúsculas y minúsculas
cantidad_vocales = 0  # Inicializa el contador de vocales
cantidad_vocales = 0  # Inicializa el contador de consonantes
cantidad_consonantes = 0  # Inicializa el contador de consonantes   

for caracter in cadena:  # Recorre cada carácter de la cadena
    if caracter in vocales:  # Verifica si el carácter es una vocal
        cantidad_vocales += 1  # Incrementa el contador de vocales
    elif caracter in consonantes:  # Verifica si el carácter es una consonante
        cantidad_consonantes += 1  # Incrementa el contador de consonantes

# Muestra los resultados
print(f"Cantidad de vocales: {cantidad_vocales}")  # Muestra la cantidad de vocales 
print(f"Cantidad de consonantes: {cantidad_consonantes}")  # Muestra la cantidad de consonantes
# Fin del ejercicio, se ha contado la cantidad de vocales y consonantes en la cadena de texto ingresada por el usuario.
