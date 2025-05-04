#Ejercicio 6: Verificación de Palíndromo Crea un programa que verifique si una palabra ingresada por el usuario es un palíndromo (se lee igual de izquierda a derecha que de derecha a izquierda).
palabra = input("Ingresa una palabra: ").lower().replace(" ", "")

if palabra == palabra[::-1]:
    print("Es un palíndromo.")
else:
    print("No es un palíndromo.")