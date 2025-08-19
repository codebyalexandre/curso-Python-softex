#3. Palavra proibida
#Peça uma frase e verifique se a palavra "bomba" aparece nela.
frase = input("Digite uma frase: ").lower()

if "bomba" in frase:
    print("A palavra bomba esta na frase")
else:
    print("A palavra bomba nao esta na frase")