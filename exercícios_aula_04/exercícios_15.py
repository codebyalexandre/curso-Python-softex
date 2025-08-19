#Questão 15 – Inversor de frase
#Peça uma frase, inverta a ordem das palavras (sem usar for ou split).

frase = input("Digite uma frase: ").strip()

palavras = []
temp = frase

while temp != "":
    if " " in temp:
        pos = temp.index(" ")
        palavra = temp[:pos]
        palavras.append(palavra)
        temp = temp[pos + 1:].strip()
    else:
        palavras.append(temp)
        temp = ""

invertida = ""
i = len(palavras) - 1
while i >= 0:
    invertida += palavras[i]
    if i != 0:
        invertida += " "
    i -= 1

print("Frase invertida:", invertida)