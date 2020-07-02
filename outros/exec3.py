nome = input("Digite seu nome: ")
vnome = len(nome)
while vnome <= 3:
    print("Insira um nome com mais de 3 caracteres: ")
    nome = input("Digite seu nome: ")
    vnome = len(nome)

idade = int(input("Digite sua idade: "))
while idade < 0 or idade > 150:
    idade = int(input("Idade invalida, digite algo entre 0 e 150: "))

salario = float(input("Informe o valor de salario: "))
while salario <= 0:
    salario = float(input("Salario invalido, digite algum valor maior que zero: "))

sexo = input("Digite o sexo, 'f' ou 'm': ")
while sexo != ("f") and sexo != ("m"):
    sexo = input("Digite sexo valido em letra menuscula: ")

estado_c = input("Digite estado civil. ('s', 'c', 'v', 'd'): ")
while estado_c != ("s") and estado_c != ("c") and estado_c != ("v") and estado_c != ("d"):
    estado_c = input("Digite estado civil valido dentro dos mencionados acima: ")

print("Nome:",nome,"\n"
      "Idade:",idade,"\n"
      "Salario:",salario,"\n"
      "Sexo:",sexo,"\n"
      "Estado civil:",estado_c)

