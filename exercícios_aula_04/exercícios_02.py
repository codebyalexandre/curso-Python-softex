#2 – Conferindo início de palavra
#Peça uma palavra e verifique com .startswith() se ela começa com "py".
#Mostre "Começa com py" ou "Não começa com py".

palavra = input("Digite uma palavra: ")

if palavra.lower().startswith("py"):
    print("Começa com py")
else:
    print("Não começa com py")