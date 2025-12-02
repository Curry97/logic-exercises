contador = 0
while True:
    contador += 1
    if contador == 3:
        print("Pulando o número 3")
        continue
    if contador == 6:
        print("Saindo do laço.")
        break
    print("Contador:", contador)