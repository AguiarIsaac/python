a4 = float(input("Informe a soma das 4 atividades: "))
a5 = float(input("Informe a nota da Prova A5: "))
media = (a4 * 0.4) + (a5 * 0.6)
if media >= 6:
    print("Ae viado, passou! A média foi:", media)
else:
    a6 = float(input("Informe a nota da prova D_Sub: "))
    new_media = (a4 * 0.4) + (a6 * 0.6)
    if new_media >= 6:
        print("Quase não passa, mas passou. Nota final", new_media)
    else:
        print("Opção feita apenas para testar pq vc vai passar em todas!")
