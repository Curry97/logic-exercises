while True:
    print("\n1 - Olá\n2 - Jogar\n3 - Sair")
    opcao = input("Escolha: ").strip()

    if opcao == "1":
        print("Olá! Bom dia.")

    elif opcao == "2":
        # Mini-jogo de adivinhação
        while True:
            t = int(input("Tente adivinhar (0-9): "))
            if t == 3:
                print("Acertou!")
                break  # sai do mini-jogo e volta ao menu
            else:
                print("Tente de novo.")

    elif opcao == "3":
        print("Saindo...")
        break  # sai do menu principal

    else:
        print("Opção inválida.")