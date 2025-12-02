# Demo 1 - break com while
print("Demo 1 - break com while")
i = 0
while True:  # loop infinito intencional
    print("i =", i)
    if i == 3:
        print("i chegou a 3 — usando break para sair")
        break  # sai do loop
    i += 1
print("Depois do loop\n")