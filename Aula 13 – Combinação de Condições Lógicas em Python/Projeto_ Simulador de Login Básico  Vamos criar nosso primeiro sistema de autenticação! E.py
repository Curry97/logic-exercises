usuario_correto = "admin"
senha_correta = "1234"

usuario = input("Usuário: ")
senha = input("Senha: ")

if usuario == usuario_correto and senha == senha_correta:
    print("Login bem-sucedido!")
else:
    print("Usuário ou senha incorretos.")