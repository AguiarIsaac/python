metros = int(input("Informe a quantidade de metros quadrados deseja pintar: "))
litros = metros / 3
latas = litros / 18
preco = latas * 80
print("De acordo com os metros quadrado informado:", metros, "\n"
      "Será necessario:", litros,"litros de tinta\n"
      "Que resulta em:", latas,"latas\n"
      "Que por sua vez custará:", float(preco),"R$")
