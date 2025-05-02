# 4.Faça um programa que leia um número e exiba sua tabuada de multiplicação (1 a 10).

n = int(input("Insira um número: "))

for i in range(1, 11): # O laço for percorre de 1 a 10
    print(f"{n} x {i} = {n*i}") # E exibe a multiplicação do número pelo valor de i
