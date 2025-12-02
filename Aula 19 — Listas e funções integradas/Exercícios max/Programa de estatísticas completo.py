n = int(input("Quantos alunos? "))
notas = []

for i in range(n):
    notas.append(float(input(f"Nota do aluno {i+1}: ")))

qtd = len(notas)
total = sum(notas)
media = total / qtd if qtd > 0 else 0.0
maior = max(notas) if qtd > 0 else None
menor = min(notas) if qtd > 0 else None

passaram = 0
for nota in notas:
    if nota >= 7.0:
        passaram += 1

print("\n--- Estatísticas ---")
print("Quantidade de alunos:", qtd)
print(f"Soma das notas: {total:.2f}")
print(f"Média: {media:.2f}")
print("Maior nota:", maior)
print("Menor nota:", menor)
print("Quantidade que passaram (>=7.0):", passaram)