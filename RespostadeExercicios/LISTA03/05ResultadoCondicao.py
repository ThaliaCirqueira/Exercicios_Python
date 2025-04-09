
# 05 Crie três variáveis lado1, lado2 e lado3 representando os lados de um triângulo. Verifique se é um triângulo equilátero (todos os lados iguais), isósceles (dois lados iguais) ou escaleno (todos os lados diferentes).. (Respondida em sala)

lado1 = int(input("Insira um valor para o primeiro lado do Triângulo: "))
lado2 = int(input("Insira um valor para o Segundo lado do Triângulo: "))
lado3 = int(input("Insira um valor para o Terceiro lado do Triângulo: "))

if lado1 == lado2 == lado3:
    print("É um triângulo equilátero, pois tem todos os lados iguais.")
elif lado1 == lado2 or lado1 == lado3 or lado2 == lado3:
    print("É um triângulo isósceles, pois tem apenas dois lados iguais.")
else:
    print("É um triângulo escaleno, pois tem todos os lados diferentes.")