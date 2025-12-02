# Demo 2 - continue com for
print("Demo 2 - continue com for (mostrar ímpares)")
for n in range(1, 11):  # 1..10
    if n % 2 == 0:
        continue  # pula números pares
    print(n, "é ímpar")
print("Fim Demo 2\n")