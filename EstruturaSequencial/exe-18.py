arquivo = int(input("Informe o tamanho do arquivo em MB: "))
velocidade = int(input("Informe a velocidade do link em Mbps: "))
tempo = arquivo / (velocidade / 8)
print(tempo)
