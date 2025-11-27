numero = 0
while numero <= 100:
    numero = int(input("Digite um número maior que 100: "))
print("Parabéns, você digitou", numero)


#Versão com Contador (Bônus)

'''''
numero = 0
tentativas = 0
while numero <= 100:
    numero = int(input("Digite um número maior que 100: "))
    tentativas = tentativas + 1
print("Parabéns! Você acertou em", tentativas, "tentativa(s).")