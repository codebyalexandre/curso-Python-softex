#Questão 13 – Sistema de login com 3 tentativas
#Usuário tem 3 tentativas para acertar login (usuário = "admin", senha = "1234"). Use .lower() para o usuário.

usuario_correto = "admin"
senha_correta = "1234"

tentativas = 3

while tentativas > 0:
    usuario = input("Usuário: ").lower()
    senha = input("Senha: ")

    if usuario == usuario_correto and senha == senha_correta:
        print("Login realizado!")
        break
    else:
        tentativas -= 1
        print("Usuário ou senha incorretos. Tentativas restantes:", tentativas)

if tentativas == 0:
    print("Acesso bloqueado!")