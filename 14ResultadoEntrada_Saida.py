
# 13 Peça a temperatura em graus Celsius e imprima a equivalente em Fahrenheit.

temperatura_celsius = float(input("Insira a temperatura em graus: "))

temperatura_Fahrenheit = (temperatura_celsius * 9/5) + 32 

print(f"A temperatura de {temperatura_celsius}C°, equivale a {temperatura_Fahrenheit:.2f} F°")