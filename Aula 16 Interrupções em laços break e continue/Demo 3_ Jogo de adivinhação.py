# Demo 3 - jogo de adivinhar número (versão simples)
print("Demo 3 - jogo: adivinhe o número (0 a 9)")
numero_secreto = 7  # número fixo para demonstração
tentativas = 0

while True:
    tentativa = int(input("Digite sua tentativa (0-9): "))
    tentativas += 1

    if tentativa == numero_secreto:
        print("Parabéns! Você acertou em", tentativas, "tentativas.")
        break  # sai do loop quando acerta
    else:
        print("Errado. Tente novamente.")

print("Fim do jogo\n")