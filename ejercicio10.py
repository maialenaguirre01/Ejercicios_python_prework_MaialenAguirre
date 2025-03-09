#Ejercicio 10: Determinar el Día de la Semana Escribe un programa que determine el día de la semana correspondiente a un número ingresado por el usuario (1 para lunes, 2 para martes, etc.).
numero = int(input("Ingresa un número del 1 al 7: "))

dias_semana = {
    1: "Lunes",
    2: "Martes",
    3: "Miércoles",
    4: "Jueves",
    5: "Viernes",
    6: "Sábado",
    7: "Domingo"
}

dia = dias_semana.get(numero, "Número no válido. Debe ser del 1 al 7.")
print(dia)