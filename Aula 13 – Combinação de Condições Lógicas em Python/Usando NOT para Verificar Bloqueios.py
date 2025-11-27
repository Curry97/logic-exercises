usuario = input("Usuário: ")
senha = input("Senha: ")
bloqueado = input("Usuário bloqueado? (s/n): ")

if usuario == "admin" and senha == "1234" and not (bloqueado == "s"):
    print("Login autorizado!")
else:
    print("Acesso negado!")