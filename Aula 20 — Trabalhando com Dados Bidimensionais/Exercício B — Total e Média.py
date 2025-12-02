# cadastro rápido ou reutilizar
produtos = []
n = int(input("Quantos produtos? "))
for i in range(n):
 produtos.append([
 input("Nome: ").strip(),
 float(input("Preço: ")),
 int(input("Qtd: "))
 ])

total = 0.0
soma_precos = 0.0
for p in produtos:
 total += p[1] * p[2]
 soma_precos += p[1]

media = soma_precos / len(produtos)

print(f"Total estoque: R$ {total:.2f}")
print(f"Preço médio: R$ {media:.2f}")