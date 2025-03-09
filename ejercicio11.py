#Ejercicio 11: Calculadora de Edad Escribe un programa que solicite al usuario su año de nacimiento y calcule su edad actual.
from datetime import date

año_nacimiento = int(input("Ingresa tu año de nacimiento: "))
año_actual = date.today().year

edad = año_actual - año_nacimiento

print(f"Tienes {edad} años.")


#datetime--> para trabajar con fechas en python
#date.today()--> extrae la fecha de hoy, y con el 'year' nos quedamos solo con el año