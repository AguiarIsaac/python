salario = float(input("Informe o valor do seu salário: "))
if salario <= 280:
    bonus = (salario * 20) / 100
    novo_s = salario + bonus
    print("Salário atual:",salario, "Bonus de 20%, que equivale a:",bonus,".",novo_s,"no total.")
elif salario <= 700:
    bonus = (salario * 15) / 100
    novo_s = salario + bonus
    print("Salário atual:",salario, "Bonus de 15%, que equivale a:",bonus,".",novo_s,"no total.")
elif salario <= 1500:
    bonus = (salario * 10) / 100
    novo_s = salario + bonus
    print("Salário atual:",salario, "Bonus de 10%, que equivale a:",bonus,".",novo_s,"no total.")
elif salario > 1500:
    bonus = (salario * 5) / 100
    novo_s = salario + bonus
    print("Salário atual:",salario, "Bonus de 5%, que equivale a:",bonus,".",novo_s,"no total.")