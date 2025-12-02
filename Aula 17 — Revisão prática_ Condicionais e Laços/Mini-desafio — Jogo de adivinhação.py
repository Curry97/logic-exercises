while True:
    numero_secreto = 7
    tentativas = 0

    while True:
        palpite = int(input("Tente adivinhar o número (0 a 10): "))
        tentativas += 1

        if palpite == numero_secreto:
            print(f"Parabéns! Você acertou em {tentativas} tentativas.")
            break
        elif palpite < numero_secreto:
            print("O número é maior.")
        else:
            print("O número é menor.")

    jogar_novamente = input("Deseja jogar novamente? (s/n): ").strip().lower()
    if jogar_novamente == "n":
        print("Encerrando o jogo. Até mais!")
        break