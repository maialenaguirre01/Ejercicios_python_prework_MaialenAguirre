#Ejercicio 2: Calculadora de Propina Crea un programa que calcule el monto total a pagar en un restaurante, incluyendo una propina del 15% sobre el total de la cuenta.
cuenta = float(input("Ingresa el total de la cuenta: €"))
propina = cuenta * 0.10
total = cuenta + propina

print(f"La propina es: €{propina:.2f}")
print(f"El total a pagar es: €{total:.2f}")