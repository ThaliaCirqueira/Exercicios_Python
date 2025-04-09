
# 13 Desenvolva um algoritmo que receba do usuário os valores a, b e c, de uma equação do segundo grau (ax^2 + bx + c = 0) e determine as raízes. (Respondida em sala)

import math

a = int(input("Digite o valor de a: "))
b = int(input("Digite o valor de b: "))
c = int(input("Digite o valor de c: "))

delta = b**2 - 4*a*c
if delta >= 0:
    x1 = (-b + math.sqrt(delta))/2*a
    x2 = (-b - math.sqrt(delta))/2*a

    sinal_de_b = '+' if b >= 0 else ''
    sinal_de_c = '+' if c >= 0 else ''
    print(f"{a}x² {sinal_de_b} {b} x + {sinal_de_c} {c} => x1 = {x1:.2f} e x2 = {x2:.2f}")
    print(f"{a} {b} {c}")

else:
    print("Não tem Raiz")
