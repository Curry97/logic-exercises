# Demo 4 - adivinhação com limite de tentativas
numero_secreto = 5
max_tentativas = 3
tentativas = 0

while tentativas < max_tentativas:
    tentativa = int(input("Digite sua tentativa: "))
    tentativas += 1

    if tentativa == numero_secreto:
        print("Você acertou! Parabéns.")
        break
    else:
        print("Errado. Restam", max_tentativas - tentativas, "tentativas.")
else:
    # Este bloco executa quando o loop termina sem break
    print("Suas tentativas acabaram. O número era", numero_secreto)