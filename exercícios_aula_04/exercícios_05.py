#5 – Substituindo palavras
#Peça uma frase e uma palavra a substituir.
#Depois peça a nova palavra e use .replace() para fazer a troca.

frase = input("Digite uma frase: ")
antiga = input("Qual palavra deseja trocar? ")
nova = input("Qual será a nova palavra? ")

frase_trocada = frase.replace(antiga, nova)
print("Frase alterada:", frase_trocada)