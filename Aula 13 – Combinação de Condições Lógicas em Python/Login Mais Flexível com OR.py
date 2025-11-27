usuario1 = "admin"
usuario2 = "professor"

usuario = input("Usuário: ")

if usuario == usuario1 or usuario == usuario2:
    print("Acesso liberado!")
else:
    print("Acesso negado!")