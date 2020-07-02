N1 = float(input("Informe a primeira nota: "))
N2 = float(input("Informe a segunda nota: "))
media = (N1 + N2) / 2
if media >= 9:
    print("Média de aproveitamento:",media,"Conceito: A --> APROVADO <--")
elif media >= 7.5:
    print("Média de aproveitamento:",media,"Conceito: B  --> APROVADO <--")
elif media >= 6:
    print("Média de aproveitamento:",media,"Conceito: C  --> APROVADO <--")
elif media >= 4:
    print("Média de aproveitamento:",media,"Conceito: D --> REPROVADO <--")
elif media <= 4:
    print("Média de aproveitamento:",media,"Conceito: E --> REPROVADO <--")
else:
    print("Error, Try gain")
    
