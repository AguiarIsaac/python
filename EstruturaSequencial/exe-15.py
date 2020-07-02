valor_hora = float(input("Por favor, informe quanto você ganha por hora: "))
hora_mes = int(input("Agora informe quantas horas você trabalha por mês: "))
salario = valor_hora * hora_mes
inss = (salario * 8) / 100
ir = (salario * 11) / 100
sindicato = (salario * 5) / 100
liquido = salario - inss - ir - sindicato
print("Slaraio Bruto:", salario,"R$\n"
      "IR (11%):", ir,"R$\n"
      "INSS (8%):", inss,"R$\n"
      "Sindicato (5%):", sindicato,"R$\n"
      "Sálario Liquido:", liquido,"R$")
