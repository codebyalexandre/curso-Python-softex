#9 – Palavra proibida com while
#Enquanto o usuário digitar algo que contenha a palavra "spoiler" (use .lower() e in), peça para digitar novamente.

texto = input("Digite um texto (não pode conter a palavra 'spoiler'): ")

while "spoiler" in texto.lower():
    print("Texto proibido! Tente novamente.")
    texto = input("Digite um texto: ")

print("Texto aceito!")