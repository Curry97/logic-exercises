'''''

Exercício 1: Percentual de aprovados

percent = (passaram / qtd) * 100 if qtd > 0 else 0.0
print(f"Percentual aprovados: {percent:.1f}%")

Exercício 2: Ler até -1 (sentinela) com while

notas = []
while True:
    nota = float(input("Digite a nota (-1 para encerrar): "))
    if nota == -1:
        break
    notas.append(nota)

if len(notas) > 0:
    print("Média:", sum(notas)/len(notas))
    print("Maior:", max(notas))
    print("Menor:", min(notas))
else:
    print("Nenhuma nota informada.")

Exercício 3: Contar notas entre 5.0 e 7.0

n = int(input("Quantas notas? "))
cont = 0
for i in range(n):
    nota = float(input("Nota: "))
    if 5.0 <= nota <= 7.0:
        cont += 1
print("Notas entre 5.0 e 7.0:", cont)

Exercício 4 (Desafio): Distribuição por faixa

n = int(input("Quantas notas? "))
faixa1 = faixa2 = faixa3 = faixa4 = 0

for i in range(n):
    nota = float(input("Nota: "))
    if nota < 5.0:
        faixa1 += 1
    elif nota < 7.0:
        faixa2 += 1
    elif nota < 9.0:
        faixa3 += 1
    else:
        faixa4 += 1

print("<5.0:", faixa1)
print("5.0-6.9:", faixa2)
print("7.0-8.9:", faixa3)
print(">=9.0:", faixa4)