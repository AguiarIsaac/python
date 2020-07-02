dia = int(input("Informe o dia: "))
mes = int(input("Informe o mês: "))
ano = int(input("Informe o ano: "))
if dia <=31 and mes <=12 and ano > 0 or ano < 0:
    print(dia,"/",mes,"/",ano,". Data válida")
else:
    print("Data inválida.")
