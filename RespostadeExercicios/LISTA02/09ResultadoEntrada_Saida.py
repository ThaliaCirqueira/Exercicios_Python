
# 9 Solicite um valor em reais e imprima o equivalente em dólares (considere a cotação fixa).

Valor_Reais = float(input("Insira um valor em Reais(R$): "))

cotacao_fixa = 5.74

valor_dolares = Valor_Reais / cotacao_fixa

print(f"O valor de R$ {Valor_Reais} em dólares é US$ {valor_dolares:.2F}")
