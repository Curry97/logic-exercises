# Demo 3 - tabuada de um número
n = int(input("Digite um número para ver sua tabuada: "))
print(f"Tabuada do {n}:")
for i in range(1, 11):
    print(f"{n} x {i} = {n * i}")
print("Fim Demo 3\n")