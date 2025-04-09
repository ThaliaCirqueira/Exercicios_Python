
# 01 Solicite ao usuário que insira um número. Se o número for positivo, exiba "Número positivo". Se for negativo, exiba "Número negativo". Se for zero, exiba "Zero".

numero = float(input("Insira um número: "))

if numero > 0:
    print("Número positivo")
elif numero < 0:
    print("Número negativo")
else:
    print("Zero")