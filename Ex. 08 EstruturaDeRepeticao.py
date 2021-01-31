def soma_e_media():
    lista = []
    contagem = 0
    soma = 0
    while contagem < 5:
        num = int(input("Informe um numero: "))
        contagem += 1 
        soma += num
        media = soma // 5
    return "A soma dos numero é: {0}, e a média dos numeros é: {1} ".format(soma,media)

print(soma_e_media())