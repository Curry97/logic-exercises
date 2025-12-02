produtos = []  # lista vazia

n = int(input("Quantos produtos deseja cadastrar? "))

for i in range(n):
    nome = input(f"Nome do produto {i+1}: ").strip()
    preco = float(input("Preço (use ponto): "))
    qtd = int(input("Quantidade: "))
    produtos.append([nome, preco, qtd])

print("\nProdutos cadastrados:")
for p in produtos:
    print(f"{p[0]} - R$ {p[1]:.2f} - Qtd: {p[2]}")