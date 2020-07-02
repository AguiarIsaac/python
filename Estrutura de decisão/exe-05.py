nota_1 = float(input("Por favor, informe a primeira nota: "))
nota_2 = float(input("Por favor, informe a Segunda nota: "))
nota_3 = float(input("Por favor, informe a terceira nota: "))
nota_4 = float(input("Por favor, informe a quarta nota: "))
media = (nota_1 + nota_2 + nota_3 + nota_4) / 4
if media == 10:
    print("Nota,", media,".Aprovado com destinção")
elif media >= 7:
    print("Nota", media, "Passou por media")
else:
    print("Que burro, dá zero pra ele")
