print("=== Calculadora de Média ===")

n1 = float(input("Primeira nota: "))
n2 = float(input("Segunda nota: "))

media = (n1 + n2) / 2
print ('Média: ', media)        # Ou limitando as casas decimais > print(f"Média: {media:.2f}")

if media >= 7:
    print("Situação: Aprovado")
elif media >= 5:
    print("Situação: Recuperação")
else:
    print("Situação: Reprovado")