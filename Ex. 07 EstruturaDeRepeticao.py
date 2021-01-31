def maior_numero():
    lista = []
    contagem = 0
    while contagem < 5:
        num = int(input("Informe um numero: "))
        lista.append(num)
        contagem += 1 
    lista
    lista_ordenada = sorted(lista)

    return lista_ordenada[-1]

print(maior_numero())
        