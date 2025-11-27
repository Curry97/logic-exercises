resposta = input("É estudante (s/n)? ")
resposta = resposta.strip().lower()

if resposta == "s":
    print("Estudante")
else:
    print("Não é estudante")


#Forma mais concisa:
''' 
resp = input("É estudante (s/n)? ").strip().lower()

if resp == "s":
    print("Estudante")
else:
    print("Não é estudante")