#Mini-Desafio:

nome = input("Digite o nome do aluno: ")
idade = int(input("Digite a idade: "))
nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))
media = (nota1 + nota2) / 2

print("\nAluno:", nome)
print("Idade:", idade)
print("Média:", media)

if media >= 7:
 print("Situação: Aprovado")
else:
 print("Situação: Reprovado")