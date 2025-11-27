n1 = float(input("Número 1: "))
n2 = float(input("Número 2: "))
n3 = float(input("Número 3: "))

# Encontrar o maior
maior = n1
if n2 > maior:
    maior = n2
if n3 > maior:
    maior = n3

# Encontrar o menor
menor = n1
if n2 < menor:
    menor = n2
if n3 < menor:
    menor = n3

print("\n=== Resultados ===")
print("Maior número:", maior)
print("Menor número:", menor)

#Solução Alternativa
'''n1 = float(input("Número 1: "))
n2 = float(input("Número 2: "))
n3 = float(input("Número 3: "))

maior = max(n1, n2, n3)
menor = min(n1, n2, n3)

print("Maior:", maior)
print("Menor:", menor)'''