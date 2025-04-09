
# 06 Peça ao usuário para inserir dois números. Se a soma dos números for maior que 100, exiba "Soma maior que 100", caso contrário, exiba "Soma menor ou igual a 100".

numero1 = float(input("Insira o primeiro número: "))
numero2 = float(input("Insira o Segundo número: "))

soma = numero1 + numero2

if soma > 100:
    print("Soma maior que 100")
else:
    print("Soma menor ou igual a 100")