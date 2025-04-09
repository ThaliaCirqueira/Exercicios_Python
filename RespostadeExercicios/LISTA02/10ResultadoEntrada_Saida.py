
# 10 Peça dois números ao usuário e imprima o resultado da divisão do primeiro pelo segundo.

Numero1 = float(input("Insira o primeiro número: "))
Numero2 = float(input("Insira o segundo número: "))

if Numero2 != 0:
    resultado = Numero1 / Numero2
    print(f"O valor da divisão de {Numero1} por {Numero2} é {resultado:.2f}")
else:
    print("Não é possivel dividir por zero")