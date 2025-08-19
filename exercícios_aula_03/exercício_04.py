#4. Login simples com validação dupla
#Peça usuário e senha.
#O login só é aceito se o usuário contiver "admin" (in) e a senha tiver no mínimo 6 caracteres (len()).

usuario = input("Digite um login")
senha = input("Digite uma senha")

if "admin" in usuario and len(senha) >= 6:
    print("Login correto")
else:
    print("Usuario ou senha invalidos")