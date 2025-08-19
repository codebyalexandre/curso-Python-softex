#10 – Centralizando texto
#Peça um texto e um número.
#Use .center() para centralizar o texto nesse tamanho usando * como preenchimento.

texto = input("Digite um texto: ")
largura = int(input("Digite a largura desejada: "))

print(texto.center(largura, "*"))