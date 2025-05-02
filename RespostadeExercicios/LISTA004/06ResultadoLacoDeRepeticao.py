# 6.Crie um programa que leia vários números até que o usuário digite 0 e mostre a soma dos números lidos.

soma = 0
numero = None

while numero != 0:  # Enquanto o número for diferente de 0, continua pedindo entradas
    numero = int(input("Insira um número: "))

    if numero != 0:  # Apenas soma se o número for diferente de 0
        soma += numero  # Adiciona o número à soma acumulada

print(f" A soma dos números é: {soma}")
