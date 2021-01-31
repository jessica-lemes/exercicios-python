n1 = float(input("Digite o primeiro número: "))
n2 = float(input("Digite o segundo número: "))
n3 = float(input("Digite o terceiro número: "))

lista = []

maior = 0

if n1 > n2 and n1 > n3:
    maior = n1
    lista.append(maior)

elif n2 > n1 and n2 > n3:
    maior = n2
    lista.append(maior)
    
elif n3 > n1 and n3 > n2:
    maior = n3
    lista.append(maior)

if n1 == maior:
    if n2 > n3:
        lista.append(n2)
        lista.append(n3)
    elif n3 > n2:
        lista.append(n3)
        lista.append(n2)

if n2 == maior:
    if n1 > n3:
        lista.append(n1)
        lista.append(n3)
    elif n3 > n1:
        lista.append(n3)
        lista.append(n1)

if n3 == maior:
    if n1 > n2:
        lista.append(n1)
        lista.append(n2)
    elif n2 > n1:
        lista.append(n2)
        lista.append(n1)


print(lista)