numero_secreto = 4
tentativas = 0

while True:
    tentativa = int(input("Tente adivinhar: "))
    tentativas += 1

    if tentativa == numero_secreto:
        print("Acertou em", tentativas, "tentativas!")
        break
    elif tentativa < numero_secreto:
        print("O número secreto é maior.")
    else:
        print("O número secreto é menor.")