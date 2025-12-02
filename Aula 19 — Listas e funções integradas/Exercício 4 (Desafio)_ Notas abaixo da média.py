notas = [5, 7, 8, 3, 9]
media = sum(notas)/len(notas)
contador = 0
for nota in notas:
 if nota < media:
contador += 1
print("Notas abaixo da média:", contador)