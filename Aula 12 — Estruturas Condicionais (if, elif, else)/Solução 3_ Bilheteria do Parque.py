idade = int(input("Idade: "))
estudante = input("É estudante (s/n)? ").strip().lower()

preco_inteiro = 40.0

if idade >= 65:
    preco = 0
elif idade <= 12 or estudante == "s":
    preco = preco_inteiro * 0.5
else:
    preco = preco_inteiro

print(f"Valor a pagar: R$ {preco:.2f}")