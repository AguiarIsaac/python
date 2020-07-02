ano = int(input("Informe o numero conrrespondente ao ano: "))
calc_1 = ano % 4
calc_2 = ano % 100
if calc_1 == 0 and calc_2 != 0:
    print(ano,"É bissexto!")
else:
    print(ano,"Não é bissexto!")

