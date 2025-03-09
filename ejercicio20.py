#Ejercicio 20: Suma de Números en una Lista Crea un programa que sume todos los números en una lista ingresada por el usuario.
numeros = input("Ingresa una lista de números separados por comas: ")
numeros_lista = [float(num) for num in numeros.split(",")]

suma = sum(numeros_lista)

print(f"La suma de los números es: {suma}")