# 1. Verificar letra na palavra
#Peça ao usuário uma palavra e depois uma letra. Informe se a letra está na palavra.

palavra = input("Digite uma palavra:")
letra = input("Digite uma letra:")

if letra in palavra:
    print("A letra esta na palavra")
else:
    print("A letra nao esta na palavra")