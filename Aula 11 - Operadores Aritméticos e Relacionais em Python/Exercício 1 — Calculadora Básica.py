a = float(input("Digite o primeiro número (A): "))
b = float(input("Digite o segundo número (B): "))

print("\n=== Resultados ===")
print("Soma:", a + b)
print("Subtração:", a - b)
print("Multiplicação:", a * b)

if b != 0:
    print("Divisão:", a / b)
else:
    print("Divisão: impossível (divisão por zero)")