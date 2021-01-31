tabuada = int(input("Informe a tabuada que deseja: "))
print("Tabuada do", tabuada)
contagem = 0

while contagem < 10:
    contagem += 1
    resultado = tabuada*contagem
    print(tabuada, "x", contagem, "=" ,resultado)
