#Ejercicio 17: Conversor de Millas a Kilómetros Escribe un programa que convierta una distancia en millas a kilómetros. Sabiendo que 1 milla equivale a 1.60934 kilómetros.
millas = float(input("Ingresa la distancia en millas: "))

kilometros = millas * 1.60934

print(f"{millas} millas equivalen a {kilometros:.2f} kilómetros.")