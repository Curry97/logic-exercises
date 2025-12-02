Mini
programa: Armazenar
nomes
e
idades

nomes = []
idades = []

for i in range(3):
    nome = input("Digite o nome: ")
    idade = int(input("Digite a idade: "))

    nomes.append(nome)
    idades.append(idade)

print("\n--- LISTA DE PESSOAS ---")
for i in range(len(nomes)):
    print(nomes[i], "-", idades[i], "anos")