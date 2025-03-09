#Ejercicio 18: Contador de Palabras Crea un programa que cuente la cantidad de palabras en una oración ingresada por el usuario.

oracion = input("Ingresa una oración: ")

palabras = oracion.split()
cantidad_palabras = len(palabras)

print(f"La oración tiene {cantidad_palabras} palabras.")


#split()--> separar por espacios para que luego cuente palabras y no letras
#len--> cuenta palabras