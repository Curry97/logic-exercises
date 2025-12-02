#Lista Estática de Produtos

#Vamos começar com uma lista já preenchida para entender como acessar os dados. Execute este código no PyCharm:

produtos = [
  ["Arroz", 12.50, 10],
  ["Feijão", 8.30, 5],
  ["Óleo", 6.00, 20]
]

print("Lista completa:")
print(produtos)

'''
Acessando Elementos

print("\nPrimeiro produto:",
      produtos[0])

print("Nome do primeiro:",
      produtos[0][0])

print("Preço do segundo:",
      produtos[1][1])

print("Qtd do terceiro:",
      produtos[2][2])

Desafio
mental: Qual
expressão
retorna
"Óleo"? Resposta: produtos[2][0