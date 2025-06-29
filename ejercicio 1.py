#EJERCICIO 1 BUSCAR NUMEROS DE UNA LISTA
#Desarrolle un algoritmo que sea capaz de encontrar un número dentro de una lista. Para esto deberás crear una lista de 10 números y solicitar al usuario que número buscar dentro de la lista.

#Importante:

#El algoritmo debe indicar si el número se encuentra en la lista o no, y en caso afirmativo, mostrar la posición del número dentro de la lista.
#El algoritmo debe manejar el caso en que el número no se encuentre en la lista, mostrando un mensaje adecuado.

lista = [36, 17, 1, 6, 5, 15, 21, 7, 2, 30] #LISTA DE NÚMERO
print("Lista de números:", lista) #MUESTRA LA LISTA DE NÚMEROS

Buscar = int(input("Ingrese el número que desea buscar: ")) #SOLICITA AL USUARIO QUE INGRESE UN NÚMERO

if Buscar in lista: #VERIFICA SI EL NÚMERO ESTÁ EN LA LISTA
    posicion = lista.index(Buscar) #OBTIENE LA POSICIÓN DEL NÚMERO EN LA LISTA
    print(f"El número {Buscar} se encuentra en la lista en la posición {posicion}.") #MUESTRA EL NÚMERO Y SU POSICIÓN 
else: #SI EL NÚMERO NO ESTÁ EN LA LISTA
    print(f"El número {Buscar} no se encuentra en la lista.") #MUESTRA UN MENSAJE INDICANDO QUE EL NÚMERO NO ESTÁ EN LA LISTA   
    
    BUCLE = input("¿Desea buscar otro número? (s/n): ") #PREGUNTA AL USUARIO SI DESEA BUSCAR OTRO NÚMERO
    
    while BUCLE.lower() == 's': #SI EL USUARIO RESPONDE 's'
    
        Buscar = int(input("Ingrese el número que desea buscar: ")) #SOLICITA AL USUARIO QUE INGRESE UN NUEVO NÚMERO
    
        if Buscar in lista:
            posicion = lista.index(Buscar)
            print(f"El número {Buscar} se encuentra en la lista en la posición {posicion}.")    
        else:
            print(f"El número {Buscar} no se encuentra en la lista.")           
        BUCLE = input("¿Desea buscar otro número? (s/n): ")
    print("Gracias por usar el buscador de números.") 
#FINALIZA EL PROGRAMA
# FIN DEL EJERCICIO 1 BUSCAR NÚMEROS DE UNA LISTA  