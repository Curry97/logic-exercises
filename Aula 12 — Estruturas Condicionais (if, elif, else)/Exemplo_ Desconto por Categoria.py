preco = float(input("Preço do produto: "))
categoria = input("Categoria (ouro/prata/bronze): ").strip().lower()

if categoria == "ouro":
    desconto = 20
elif categoria == "prata":
    desconto = 10
elif categoria == "bronze":
    desconto = 5
else:
    desconto = 0

print("Desconto:", desconto, "%")
print("Preço final:", preco - (preco * desconto / 100))