valor_hambúrguer = 40.00
cupom_desconto ="desconto"

while True:
    lanche = input("Qual lanche você deseja?")
    if lanche =="hambúrguer":
        print("Pedido confirmado")
        break
    else:
        print("Este lanche não está cadastrado, tente novamente.")

cupom = input("Digite seu cupom de desconto:")
if cupom ==cupom_desconto:
    print(f"Seu lanche custou {valor_hambúrguer*0.8}")
else:
    print(f"Seu lanche custou{valor_hambúrguer}")
    