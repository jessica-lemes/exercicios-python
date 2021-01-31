lista = []
numeros = -1

while numeros != 0:
        numeros = int(input("Informe um número ou digite 0 para sair: "))
        if numeros != 0:
            if numeros < 0 or numeros > 1000:
                print("Informe apenas numeros maiores que 0 e menores que 1000 ")
            else:
                lista.append(numeros)
        else:
            print("Volte sempre")

lista.sort()
soma = 0
for i in lista:
    soma += i

print("Menor =", lista[0], ", Maior =", lista[-1], ", Soma =",soma)