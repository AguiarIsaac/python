nome = input("Digite seu nome: ")
senha = input("Digite sua senha: ")
while nome == senha:
    print("Usuario e senha iguais, Favor, digitar senha diferente no nome de usuario: ")
    nome = input("Digite seu nome: ")
    senha = input("Digite sua senha: ")
else:
    print("Senha e usuario validos!")
