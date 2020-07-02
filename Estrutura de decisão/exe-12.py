hora = int(input("Informe quantas horas mensais trabalhadas: "))
valorHora = float(input("Informe o valor da hora: "))
salarioBruto = valorHora * hora

if salarioBruto <= 900:
    inss = (salarioBruto * 10 ) / 100
    fgts = (salarioBruto * 11 ) / 100
    sindicato = (salarioBruto * 3) / 100
    totalDescontos = inss + sindicato
    salarioLiquido = salarioBruto - totalDescontos
    print("Salário Bruto->     : R$",salarioBruto, "\n"
          "(-) IR (5%)->       : R$ ISENTO\n"
          "(-) INSS (1O%)->    : R$",inss,"\n"
          "(-) FGTS (11%)->    : R$",fgts,"\n"
          "Total de descontos  : R$",totalDescontos,"\n"
          "Salário liquido->   : R$",salarioLiquido)

elif salarioBruto <= 1500:
    ir = (salarioBruto * 5) / 100
    inss = (salarioBruto * 10 ) / 100
    fgts = (salarioBruto * 11 ) / 100
    sindicato = (salarioBruto * 3) / 100
    totalDescontos = inss + sindicato + ir
    salarioLiquido = salarioBruto - totalDescontos
    print("Salário Bruto->     : R$",salarioBruto, "\n"
          "(-) IR (5%)->       : R$",ir,"\n"
          "(-) INSS (1O%)->    : R$",inss,"\n"
          "(-) FGTS (11%)->    : R$",fgts,"\n"
          "Total de descontos  : R$",totalDescontos,"\n"
          "Salário liquido->   : R$",salarioLiquido)

elif salarioBruto <= 2500:
    ir = (salarioBruto * 10) / 100
    inss = (salarioBruto * 10 ) / 100
    fgts = (salarioBruto * 11 ) / 100
    sindicato = (salarioBruto * 3) / 100
    totalDescontos = inss + sindicato + ir
    salarioLiquido = salarioBruto - totalDescontos
    print("Salário Bruto->     : R$",salarioBruto, "\n"
          "(-) IR (10%)->      : R$",ir,"\n"
          "(-) INSS (1O%)->    : R$",inss,"\n"
          "(-) FGTS (11%)->    : R$",fgts,"\n"
          "Total de descontos  : R$",totalDescontos,"\n"
          "Salário liquido->   : R$",salarioLiquido)

elif salarioBruto > 2500:
    ir = (salarioBruto * 20) / 100
    inss = (salarioBruto * 10 ) / 100
    fgts = (salarioBruto * 11 ) / 100
    sindicato = (salarioBruto * 3) / 100
    totalDescontos = inss + sindicato + ir
    salarioLiquido = salarioBruto - totalDescontos
    print("Salário Bruto->     : R$",salarioBruto, "\n"
          "(-) IR (20%)->      : R$",ir,"\n"
          "(-) INSS (1O%)->    : R$",inss,"\n"
          "(-) FGTS (11%)->    : R$",fgts,"\n"
          "Total de descontos  : R$",totalDescontos,"\n"
          "Salário liquido->   : R$",salarioLiquido)

else:
    print("Tente novamente")
