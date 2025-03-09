#Ejercicio 4: Contador de Vocales Crea un programa que cuente el número de vocales en una palabra ingresada por el usuario.
palabra = input("Ingresa una palabra: ").lower()
vocales = "aeiou"
contador = 0

for letra in palabra:
    if letra in vocales:
        contador += 1

print(f"La palabra '{palabra}' tiene {contador} vocales.")