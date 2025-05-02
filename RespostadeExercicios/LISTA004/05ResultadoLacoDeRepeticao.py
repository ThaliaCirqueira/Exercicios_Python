# 5.Escreva um programa que conte quantos números entre 1 e 100 são pares.

lista = []  # Cria uma lista vazia para armazenar os números pares

for i in range(1, 101):  # Loop percorre de 1 a 100
    # Verifica se 'i' é par (divisível por 2). Filtra somente os números pares (um número é par se o resto da divisão por 2 for 0)
    if i % 2 == 0:
        lista.append(i)  # Sempre que i for par, ele é armazenado na lista.
print(len(lista))  # Exibe a quantidade de números pares armazenados na lista
