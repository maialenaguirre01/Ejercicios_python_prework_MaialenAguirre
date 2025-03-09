#Ejercicio 13: Verificación de Número Primo Escribe un programa que determine si un número ingresado por el usuario es primo o no.
numero = int(input("Ingresa un número: "))

if numero > 1:
    es_primo = True
    for i in range(2, int(numero ** 0.5) + 1):
        if numero % i == 0:
            es_primo = False
            break
    
    if es_primo:
        print(f"{numero} es un número primo.")
    else:
        print(f"{numero} no es un número primo.")
else:
    print(f"{numero} no es un número primo.")

#Recorremos los posibles divisores, desde 2 hasta la raíz cuadrada del número (numero ** 0.5).
#Esto optimiza el algoritmo, porque si un número no tiene divisores hasta su raíz cuadrada, ya no los tendrá después.
# % (módulo) nos dice si hay residuo en la división.