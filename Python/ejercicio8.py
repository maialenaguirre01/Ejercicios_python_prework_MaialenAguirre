#Ejercicio 8: Cálculo del Índice de Masa Corporal (IMC) Escribe un programa que calcule el Índice de Masa Corporal (IMC) de una persona.
peso = float(input("Ingresa tu peso en kilogramos: "))
altura = float(input("Ingresa tu altura en metros: "))

imc = peso / (altura ** 2)

print(f"Tu IMC es: {imc:.2f}")

if imc < 18.5:
    print("Estado: Bajo peso")
elif 18.5 <= imc < 24.9:
    print("Estado: Peso normal")
elif 25 <= imc < 29.9:
    print("Estado: Sobrepeso")
else:
    print("Estado: Obesidad")