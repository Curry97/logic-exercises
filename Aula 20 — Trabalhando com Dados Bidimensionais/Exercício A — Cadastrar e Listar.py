produtos = []
n = int(input("Quantos produtos? "))

for i in range(n):
    nome = input(f"Nome {i+1}: ").strip()
    preco = float(input("Preço: "))
    qtd = int(input("Quantidade: "))
    produtos.append([nome, preco, qtd])

print("\n--- Produtos cadastrados ---")
for i in range(len(produtos)):
    p = produtos[i]
    print(f"{i+1}. {p[0]} - "
          f"R$ {p[1]:.2f} - Qtd: {p[2]}")