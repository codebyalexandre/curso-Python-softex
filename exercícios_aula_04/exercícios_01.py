#1 – Comparando nomes ignorando maiúsculas
#Peça dois nomes e verifique se são iguais usando .lower().
#Se forem iguais, mostre "Nomes iguais", senão "Nomes diferentes".

nome1 = input("Digite o primeiro nome: ")
nome2 = input("Digite o segundo nome: ")

if nome1.lower() == nome2.lower():
    print("Nomes iguais")
else:
    print("Nomes diferentes")