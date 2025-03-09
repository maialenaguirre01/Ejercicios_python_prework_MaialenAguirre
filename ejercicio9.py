#Ejercicio 9: Conversor de Divisas Crea un programa que convierta una cantidad de dólares a euros. Suponiendo que 1 dólar es igual a 0.85 euros.
tasa_cambio = 0.85

dolares = float(input("Ingresa la cantidad en dólares: $"))
euros = dolares * tasa_cambio

print(f"${dolares:.2f} dólares equivalen a €{euros:.2f} euros")