
# 12 Crie um programa que simula o jogo Pedra, Papel e Tesoura. Receba a escolha do usuário e compare com uma escolha aleatória do computador. (Respondida em sala)
import random

usuario = input("pedra ou papel ou tesoura?: ").lower()

valor_aleatorio = random.randint(1, 3)

if valor_aleatorio == 1:
    computador = "pedra"
elif valor_aleatorio == 2:
    computador = "papel"
else:
    computador = "tesoura"

voce_ganhou = (usuario == "pedra" and computador == "tesoura") or \
              (usuario == "papel" and computador == "pedra") or \
              (usuario == "tesoura" and computador == "papel")

if voce_ganhou:
    print("Você ganhou!")
elif usuario == computador:
    print("Empate")
else:
    print("Você perdeu!")
