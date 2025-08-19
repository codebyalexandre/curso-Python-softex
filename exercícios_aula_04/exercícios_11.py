#11 – Validador de Senha Forte
#Peça uma senha e valide que ela tenha:

#pelo menos 8 caracteres

#pelo menos 1 letra maiúscula

#pelo menos 1 letra minúscula

#pelo menos 1 número

#pelo menos 1 símbolo (não letra nem número)

senha = input("Digite sua senha: ")

tem_maiuscula = False
tem_minuscula = False
tem_numero = False
tem_simbolo = False

i = 0
while i < len(senha):
    caractere = senha[i]

    if caractere.isupper():
        tem_maiuscula = True
    elif caractere.islower():
        tem_minuscula = True
    elif caractere.isdigit():
        tem_numero = True
    elif not caractere.isalnum():
        tem_simbolo = True

    i += 1  # i = i + 1

if len(senha) >= 8 and tem_maiuscula and tem_minuscula and tem_numero and tem_simbolo:
    print("Senha forte!")
else:
    print("Senha fraca! Deve conter:")
    print("- Pelo menos 8 caracteres")
    print("- Letra maiúscula")
    print("- Letra minúscula")
    print("- Número")
    print("- Símbolo")