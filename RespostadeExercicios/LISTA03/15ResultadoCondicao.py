
# 15 Crie um programa dado solicite a largura e o comprimento de uma sala (supondo que a sala seja quadrática), solicite a largura e o tamanho do piso e mostre quantos peças do preciso será necessário para revestir toda a sala.. (Respondida em sala)

largura_sala = int(input("Qual a largura da sala, em cm: "))
comprimento_sala = int(input("Qual comprimento da sala, em cm: "))
largura_piso = int(input("Qual a largura do piso, em cm: "))
comprimento_piso = int(input("Qual comprimento do piso, em cm: "))
margem_de_erro = int(input("Qual a porcentagem de piso a mais que você quer comprar: "))

percentual = (1 + (margem_de_erro/100))

area_sala = largura_sala * comprimento_sala
area_piso = largura_piso * comprimento_piso

total_de_piso = (area_sala // area_piso)
total_com_margem = total_de_piso * percentual

print(f"Você vai precisar de {total_de_piso} pisos, com margem de erro {total_com_margem:.0f}")