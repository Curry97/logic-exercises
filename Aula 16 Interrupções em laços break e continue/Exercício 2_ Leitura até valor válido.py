soma = 0

while True:
    n = int(input("Digite um inteiro (0 para encerrar): "))

    if n < 0:
        print("Valor inválido — não aceitamos negativos.")
    continue  # volta ao início do loop

    if n == 0:
        break  # encerra o loop

    soma += n

print("Soma total:", soma)