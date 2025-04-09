
# 10 Crie um programa que recebe três números do usuário e determina qual é o maior número, utilizando apenas condicionais..

numero1 = int(input("Insira o primeiro número: "))
numero2 = int(input("Insira o segundo número: "))
numero3 = int(input("Insira o terceiro número: "))

if numero1 > numero2 and numero1 > numero3:
    print(f"O número {numero1} é maior")
elif numero2 > numero1 and numero2 > numero3:
    print(f"O número {numero2} é maior")
else:
    print(f"O número {numero3} é maior")