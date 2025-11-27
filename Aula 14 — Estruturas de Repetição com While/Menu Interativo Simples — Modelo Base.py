opcao = ""
while opcao != "3":
    print("Menu Principal")
    print("1 - Dizer olá")
    print("2 - Mostrar uma dica")
    print("3 - Sair")
    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        print("Olá, seja bem-vindo!")
    elif opcao == "2":
        print("Dica: pratique lógica todos os dias!")
    elif opcao != "3":
        print("Opção inválida!")

print("Programa encerrado.")