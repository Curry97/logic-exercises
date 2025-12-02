n = int(input("Quantas notas? "))
notas = []
for i in range(n):
 notas.append(float(input("Nota: ")))

maior = max(notas)
menor = min(notas)
media = sum(notas)/len(notas)
acima = 0
for nota in notas:
 if nota > media:
 acima += 1

print("Maior:", maior)
print("Menor:", menor)
print(f"Média: {media:.2f}")
print("Acima da média:", acima)