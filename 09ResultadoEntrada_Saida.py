
# 1 Solicite ao usuário que insira seu nome e imprima uma mensagem de saudação.
nome = input("Digite seu nome: ")
# 2 Solicite a idade do usuário e imprima uma mensagem indicando se é maior de idade.
idade = int(input("Insira sua idade: "))


print("Olá", nome, "Que sua jornada aqui seja repleta de Luz! Bem vindo(a)!")

if idade >= 18:
    print("Você é maior de idade!")
else:
    print("Você não é maior de idade")
