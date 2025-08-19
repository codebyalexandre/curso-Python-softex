#8 – Senha com validação de letras e/ou números
#Peça uma senha e verifique com .isalnum() se ela contém apenas letras e/ou números.
#Se for válido, mostre "Senha válida", senão "Senha inválida".

senha = input("Digite sua senha: ")

if senha.isalnum():
    print("Senha válida")
else:
    print("Senha inválida (use apenas letras e números)")