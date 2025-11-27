while True:
    print("\nMENU")
    print("1 - Calculadora de Média")
    print("2 - Operações Básicas")
    print("3 - Sair")
    opcao = input("Escolha uma opção: ")


    if opcao == "1":
        print("\nCalculadora de Média ")
        nota1 = float(input("Digite a primeira nota: "))
        nota2 = float(input("Digite a segunda nota: "))

        media = (nota1 + nota2) / 2
        print(f"Média: {media:.2f}")

        if media >= 7:
            print("Situação: APROVADO")
        elif media >= 5:
            print("Situação: RECUPERAÇÃO")
        else:
            print("Situação: REPROVADO")


    elif opcao == "2":
        print("\nOperações Básicas")
        n1 = float(input("Digite o primeiro número: "))
        n2 = float(input("Digite o segundo número: "))

        print(f"Soma: {n1 + n2}")
        print(f"Subtração: {n1 - n2}")
        print(f"Multiplicação: {n1 * n2}")

        if n2 != 0:
            print(f"Divisão: {n1 / n2}")
        else:
            print("Divisão: impossível (divisão por zero)")


    elif opcao == "3":
        print("\nSaindo... Obrigado por usar o programa!")
        break

    else:
        print("Opção inválida! Tente novamente.")
