valor_1 = int(input("Informe o primeiro valor: "))
valor_2 = int(input("Informe o segundo valor: "))
valor_3 = int(input("Informe o terceiro valor: "))
if valor_1 < valor_2 and valor_2 < valor_3:
    print(valor_1, valor_2, valor_3)
elif valor_2 < valor_1 and valor_1 < valor_3:
    print(valor_2, valor_1, valor_3)
elif valor_3 < valor_2 and valor_2 < valor_1:
    print(valor_3, valor_2, valor_1)
else:
    print("Tente novamente")
