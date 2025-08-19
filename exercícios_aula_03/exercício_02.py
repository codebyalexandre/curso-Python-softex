#2. Senha mínima
#Solicite uma senha e verifique se ela tem pelo menos 8 caracteres usando len().

senha = input("Digite a sua senha:")

if len(senha) < 8:
    print("A senha deve ter mais que 8 caracteres")
else:
    print("Senha cadastrada")