Valor Total do Estoque

total = 0.0
for p in produtos:
    total += p[1] * p[2]

print(f"Valor total: R$ {total:.2f}")

''''
Produto Mais Caro

mais_caro = produtos[0]
for p in produtos:
    if p[1] > mais_caro[1]:
        mais_caro = p

print(f"Mais caro: {mais_caro[0]}")
print(f"Preço: R$ {mais_caro[1]:.2f}")