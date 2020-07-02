produto_1 = float(input("Informe o valor do primeiro produto: "))
produto_2 = float(input("Informe o valor do segundo produto: "))
produto_3 = float(input("Informe o valor do terceiro produto: "))
if produto_1 < produto_2 and produto_1 < produto_3:
    print("O produto mais barato custa:", produto_1)
elif produto_2 < produto_1 and produto_2 < produto_3:
    print("O produto mais barato custa", produto_2)
else:
    print("O produto mais barato custo", produto_3)
