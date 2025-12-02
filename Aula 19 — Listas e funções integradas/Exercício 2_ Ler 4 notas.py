notas = []
for i in range(4):
    notas.append(float(input("Nota: ")))
media = sum(notas) / len(notas)
print(f"Média: {media:.2f}")