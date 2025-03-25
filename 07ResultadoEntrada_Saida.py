
# 7 Solicite a altura e o peso do usuário. Calcule o IMC (Índice de Massa Corporal) e imprima o resultado.

altura = float(input("Insira sua altura (em metros): "))
peso = float(input("Insira seu peso (em kg): "))

imc = peso / (altura ** 2)

print(f"Seu IMC é: {imc:.2f}")