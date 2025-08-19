#Questão 17 – Extrator de números
#Peça um texto e extraia só os números, mostrando-os em sequência.

texto = input("Digite um texto: ")
numeros = ""
i = 0

while i < len(texto):
    if texto[i].isdigit():
        numeros += texto[i]
    i += 1

print("Números encontrados:", numeros)