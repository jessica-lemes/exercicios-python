termo = int(input("Informe quantos termo Fibonacci deseja que seja calculado: "))
anterior = 0
proximo = 0
contador = 1
while contador <= termo:
    
    print(proximo)
    proximo = proximo + anterior
    anterior = proximo - anterior 
    contador += 1

    if(proximo == 0):
        proximo = proximo + 1