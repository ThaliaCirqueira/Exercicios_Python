
# 07 Crie uma variável mes e atribua um valor de 1 a 12 representando um mês. Exiba o nome do mês correspondente (por exemplo, se mes for 1, exiba "Janeiro").  

mes = int(input("Insira um número de 1 a 12 e descubra o mês correspondente: "))

if mes == 1:
    print("Janeiro")
elif mes == 2:
    print("Fevereiro")
elif mes == 3:
    print("Março")
elif mes == 4:
    print("Abril")
elif mes == 5:
    print("Maio")
elif mes == 6:
    print("Junho")
elif mes == 7:
    print("Julho")
elif mes == 8:
    print("Agosto")
elif mes == 9:
    print("Setembro")
elif mes == 10:
    print("Outubro")
elif mes == 11:
    print("Novembro")
elif mes == 12:
    print("Dezembro")
else:
    print("Número invalido. Insira um numero entre 1 e 12")