valor_1 = int(input("Informe o primeiro valor: "))
valor_2 =  int(input("Informe o segundo valor: "))
valor_3 =  int(input("Informe o terceiro valor: "))
if valor_1 > valor_2 and valor_1 > valor_3:
    maior = valor_1
elif valor_2 > valor_1 and valor_2 > valor_3:
    maior = valor_2
elif valor_3 > valor_1 and valor_3 > valor_2:
    maior = valor_3
if valor_1 < valor_2 and valor_1 < valor_3:
    menor = valor_1
elif valor_2 < valor_1 and valor_2 < valor_3:
    menor = valor_2
elif valor_3 < valor_1 and valor_3 < valor_2:
    menor = valor_3
print("Maior:", maior, "e o menor:", menor)
