#Ejercicio 14: Calculadora de Descuento Crea un programa que calcule el precio final de un artículo después de aplicar un descuento del 20%.
precio_original = float(input("Ingresa el precio original del artículo: $"))
descuento = 0.20

precio_final = precio_original * (1 - descuento)

print(f"El precio final con descuento es: ${precio_final:.2f}")