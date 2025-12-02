nome_venda = input("Nome do produto vendido: ").strip()
qtd_vendida = int(input("Quantidade vendida: "))

encontrado = False
for i in range(len(produtos)):
    if produtos[i][0].lower() == nome_venda.lower():
        encontrado = True
        produtos[i][2] -= qtd_vendida
        print(f"Quantidade atualizada: {produtos[i][2]} unidades")

        if produtos[i][2] <= 0:
            produtos.pop(i)
            print("Produto esgotado e removido do cadastro.")
        break

if not encontrado:
    print("Produto não encontrado.")