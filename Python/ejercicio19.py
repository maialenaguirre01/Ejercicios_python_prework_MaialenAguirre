#Ejercicio 19: Verificación de Año Bisiesto Escribe un programa que determine si un año ingresado por el usuario es bisiesto o no.
año = int(input("Ingresa un año: "))

if (año % 4 == 0 and año % 100 != 0) or (año % 400 == 0):
    print(f"{año} es un año bisiesto.")
else:
    print(f"{año} no es un año bisiesto.")