num_1 = int(input("Informe o primeiro numero: "))
num_2 = int(input("Informe o segundo numero: "))
num_3 = int(input("Informe o terceiro numero: "))
soma = num_1 + num_2
soma1 = num_2 + num_3
if soma > num_3 or soma1 >= soma:
    if num_1 == num_2 and num_2 == num_3:
        print("Triangulo equilátero")
    elif num_1 == num_2 or num_1 == num_3 or num_2 == num_3:
        print("Triangulo isóceles")
    elif num_1 != num_2 and num_1 != num_3 and num_3 != num_2:
        print("Triangulo escaleno")
else:
    print("Error, Try gain")
