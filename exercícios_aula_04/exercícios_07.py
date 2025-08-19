#7 – Verificação de número
#Peça algo ao usuário e use .isdigit() para verificar se ele digitou apenas números.

valor = input("Digite algo: ")

if valor.isdigit():
    print("Você digitou apenas números.")
else:
    print("Não é apenas número.")