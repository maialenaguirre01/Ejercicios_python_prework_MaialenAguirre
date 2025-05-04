#Ejercicio 16: Contador de Números Pares e Impares Crea un programa que cuente y muestre la cantidad de números pares e impares en una lista ingresada por el usuario
numeros = input("Ingresa una lista de números separados por comas: ")
numeros_lista = [int(num) for num in numeros.split(",")]

pares = sum(1 for num in numeros_lista if num % 2 == 0)
impares = len(numeros_lista) - pares

print(f"Números pares: {pares}")
print(f"Números impares: {impares}")

#input--> numeros = "4,7,2,9,12"
# numeros.split(",")--> ['4', '7', '2', '9', '12']
# [int(num) for num in numeros.split(",")]--> [4, 7, 2, 9, 12]
  #Recorre cada elemento de la lista con for num in ....
  #Convierte cada elemento a entero con int(num).

# pares = sum(1 for num in numeros_lista if num % 2 == 0)
  # Por cada número par, genera un 1 --> Para la lista [4, 7, 2, 9, 12], el generador produciría:1, 1, 1

  # bucle tradicional
pares = 0
for num in numeros_lista:
    if num % 2 == 0:
        pares += 1