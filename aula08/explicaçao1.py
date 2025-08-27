num = "21970661246"
valido =True
for c in num:
    contador_repetidos = 0
    for d in num:
        print(f"num c{c} num d {d} são iguais? {c==d}")
        if c==d:
            contador_repetidos+=1
            if contador_repetidos >=3:
                print("Número não é valido")
                valido = False
                break