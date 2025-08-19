#Peça ao usuário a idade. Depois confirme:
# - Se a pessoa ainda não pode votar (idade menor que 16)
# - Se o voto é opcional (16 ou 17 anos, ou mais de 70)
# - Se o voto é obrigatório (entre 18 e 70 anos, inclusive)

# idade = int(input("Qual a sua idade: "))

# if idade < 16:
#     print("Você não pode votar")
# elif idade >= 16 and idade <= 17 or idade >= 70:
#     print("Seu voto é opcional")
# else:
#     print("Seu voto é obrigatório")

preco = float(input("Digite o valor do produto"))
if preco > 100:
    desconto = preco * 0.1
    novoPreco = preco - desconto
    print(f"O novo valor é {novoPreco}")
else:
    print("Preço sem desconto")