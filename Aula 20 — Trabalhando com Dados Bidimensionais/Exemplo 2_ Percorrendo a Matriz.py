produtos = [
  ["Arroz", 12.50, 10],
  ["Feijão", 8.30, 5],
  ["Óleo", 6.00, 20]
]

print("--- Cadastro de Produtos ---")
for i in range(len(produtos)):
    linha = produtos[i]
    nome = linha[0]
    preco = linha[1]
    qtd = linha[2]
    print(f"{i+1}. {nome} - R$ {preco:.2f} - Qtd: {qtd}")