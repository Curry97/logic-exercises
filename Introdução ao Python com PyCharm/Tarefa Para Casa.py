produto1 = input("Digite o nome do produto 1: ")
produto2 = input("Digite o nome do produto 2: ")
produto3 = input("Digite o nome do produto 3: ")

valorProduto1 = float(input("Digite o valor do produto 1: "))
valorProduto2 = float(input("Digite o valor do produto 2: "))
valorProduto3 = float(input("Digite o valor do produto 3: "))

maisCaro = produto1
maiorPreco = valorProduto1

if valorProduto2 > maiorPreco:
    maisCaro = produto2
    maiorPreco = valorProduto2

if valorProduto3 > maiorPreco:
    maisCaro = produto3
    maiorPreco = valorProduto3

print(f"Esse produto é o mais caro: {maisCaro}")


