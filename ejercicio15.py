#Ejercicio 15: Conversor de Tiempo Escribe un programa que convierta un número de minutos en horas y minutos. Por ejemplo, 145 minutos serían 2 horas y 25 minutos.
minutos_totales = int(input("Ingresa la cantidad de minutos: "))

horas = minutos_totales // 60
minutos_restantes = minutos_totales % 60

print(f"{minutos_totales} minutos son {horas} horas y {minutos_restantes} minutos.")

# // devuelve solo la aparte entera del cociente.
# % (módulo) te da el residuo de la división: lo que sobra después de formar las horas completas