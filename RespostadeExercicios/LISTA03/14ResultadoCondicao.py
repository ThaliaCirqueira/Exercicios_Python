
# 14 Elabore um algoritmo que recebe 05 bits individualmente de um número binário e mostre o número decimal.

numero = float(input("Insira um número: "))

if numero > 0:
    print("Número positivo")
elif numero < 0:
    print("Número negativo")
else:
    print("Zero")