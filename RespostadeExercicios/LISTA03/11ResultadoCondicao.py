
# 11 Implemente um programa que solicita ao usuário o ano de nascimento e classifica a faixa etária em "Criança", "Adolescente", "Adulto Jovem" ou "Adulto".

ano_nascimento = int(input("Insira seu ano de nascimento: "))

ano_atual = 2025

idade = ano_atual - ano_nascimento 


if idade <=12 : 
    print("CRIANÇA")
elif 12 <= idade <= 17 : 
    print("ADOLESCENTE")
elif 18 <= idade <=35 : 
    print("ADULTO JOVEM")
else:
    print("ADULTO")