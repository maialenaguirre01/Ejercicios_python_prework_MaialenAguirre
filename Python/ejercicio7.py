#Ejercicio 7: Calculadora Simple Crea un programa que realice operaciones aritméticas simples (suma, resta, multiplicación, división) según la elección del usuario.
print("Calculadora Simple")
print("1. Suma")
print("2. Resta")
print("3. Multiplicación")
print("4. División")

opcion = input("Elige una opción (1-4): ")

num1 = float(input("Ingresa el primer número: "))
num2 = float(input("Ingresa el segundo número: "))

if opcion == "1":
    resultado = num1 + num2
    print(f"La suma es: {resultado}")
elif opcion == "2":
    resultado = num1 - num2
    print(f"La resta es: {resultado}")
elif opcion == "3":
    resultado = num1 * num2
    print(f"La multiplicación es: {resultado}")
elif opcion == "4":
    if num2 != 0:
        resultado = num1 / num2
        print(f"La división es: {resultado}")
    else:
        print("No se puede dividir entre cero.")
else:
    print("Opción no válida.")