numero_secreto = 7
tentativas = 0
acertou = False

while not acertou:
    tentativa = int(input("Sua tentativa: "))
    tentativas += 1

    if tentativa == numero_secreto:
        acertou = True
        print("Acertou em", tentativas, "tentativas!")
    else:
        print("Tente de novo...")