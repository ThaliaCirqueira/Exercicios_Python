
# 14 Elabore um algoritmo que recebe 05 bits individualmente de um número binário e mostre o número decimal.(Respondida em sala)

bits = []

bit0 = int(input("Digite o bit 0: "))
bit1 = int(input("Digite o bit 1: "))
bit2 = int(input("Digite o bit 2: "))
bit3 = int(input("Digite o bit 3: "))
bit4 = int(input("Digite o bit 4: "))

if (bit0 not in [0, 1] or
    bit1 not in [0, 1] or
    bit2 not in [0, 1] or
    bit3 not in [0, 1] or
    bit4 not in [0, 1]):
    print("Números binários são compostos apenas pelos digitos 0 e 1.")
else:
    bits.append(bit0)
    bits.append(bit1)
    bits.append(bit2)
    bits.append(bit3)
    bits.append(bit4)

decimal = bits[0]*16 + bits[1]*8 + bits[2]*4 + bits [3]*2 + bits[4]*1

print("O número decimal correspondente é :", decimal)