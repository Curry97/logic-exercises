# Imprime tabuadas de 2, 3 e 4
for n in range(2, 5): # Para as tabuadas do 2, 3 e 4
    print(f"\n--- Tabuada do {n} ---")
    for i in range(1, 11): # Para os números de 1 a 10
        print(f"{n} x {i} = {n * i}")