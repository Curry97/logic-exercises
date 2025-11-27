def classifica_idade(idade):
    if idade <= 12:
        return "Criança"
    elif idade <= 17:
        return "Adolescente"
    elif idade <= 59:
        return "Adulto"
    else:
        return "Idoso"

# Programa principal
idade_usuario = int(input("Idade: "))
categoria = classifica_idade(idade_usuario)
print(f"Você é: {categoria}")