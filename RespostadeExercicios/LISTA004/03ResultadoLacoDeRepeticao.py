# 3.Solicite 10 números ao usuário e exiba a média aritmética

numero = []  # Cria uma lista vazia para armazenar os números


for i in range(10): # Laço 'for' que se repete 10 vezes
    entrada = float(input("Insira um número: ")) # Solicita um número e converte para 'float'
    numero.append(entrada) # Adiciona o número à lista

media = sum(numero) / len(numero) # Calcula a média aritmética
print(f"A média aritmética do número digitado é: {media:.2f}") # Exibe a média com duas casas decimais

