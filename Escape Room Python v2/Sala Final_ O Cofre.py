
notas = []
for i in range(4):
    nota = float(input(f"Digite a {i+1}ª nota: "))
    notas.append(nota)


qnt = len(notas)
notaMaior = max(notas)
notaMenor = min(notas)
media = sum(notas) / qnt


print(f"Notas: {notas}")
print(f"Quantidade de notas: {qnt}")
print(f"Média: {media:.2f}")
print(f"Maior nota: {notaMaior}")
print(f"Menor nota: {notaMenor}")