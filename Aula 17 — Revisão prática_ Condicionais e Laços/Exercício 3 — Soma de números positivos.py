soma = 0
for i in range(5):
    numero = int(input("Digite um número: "))
    if numero < 0:
        continue
    soma += numero
print("Soma dos números positivos:", soma)