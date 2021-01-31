lista = []
numeros = -1
while numeros != 0:
    numeros = int(input("Informe um número ou digite 0 para sair: "))
    if numeros != 0:
        lista.append(numeros)
    else:
        print("Volte sempre")


lista.sort()

soma = 0
for i in lista:
    soma += i


print("Menor =", lista[0], ", Maior =", lista[-1], ", Soma =",soma)