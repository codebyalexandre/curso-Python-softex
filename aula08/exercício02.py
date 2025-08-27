numero = input("Digite o número de telefone com 11 dígitos: ")

if len(numero) != 11:
    print("Array com tamanho incorreto.")
elif not numero.isdigit():
    print("Não é possível gerar um número de telefone com esses valores.")
else:
    valido = True

    for c in numero:
        cont = numero.count(c)
        if cont >= 3:
            valido = False
            break

    if not valido:
        print("Não é possível gerar um número de telefone com esses valores.")
    else:
  
        telefone_formatado = f"({numero[0]}{numero[1]}){numero[2]}{numero[3]}{numero[4]}{numero[5]}{numero[6]}-{numero[7]}{numero[8]}{numero[9]}{numero[10]}"
        print(telefone_formatado)
