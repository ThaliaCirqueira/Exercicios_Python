
# 08 Crie uma variável ano e atribua um valor numérico. Verifique se o ano é bissexto. Se for, exiba "Ano bissexto", caso contrário, exiba "Ano não bissexto".

#Somente anos divisiveis por 4 podem ser Bissextos.Anos divisiveis por 100 não são bissextos.

ano = int(input("Insira o ano para descobrir se ele é bissexto ou não: "))

if (ano % 4 == 0 and ano % 100 != 0) or (ano % 400 == 0):
    print("Ano Bissexto")
else:
    print ("Ano não Bissexto")