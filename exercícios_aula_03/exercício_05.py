#5. Contador de caracteres e verificação de letra
#Peça uma palavra e mostre:
#Quantos caracteres ela tem (len())
#Se "a" está nela (in)

palavra = input("Digite uma palavra:")

tamanho = len(palavra)

print(f"tamanho da palavra: {tamanho}")

if "a" in palavra:
    print("A letra A está na palavra!!")
else:
    print("A letra A não está na palavra")