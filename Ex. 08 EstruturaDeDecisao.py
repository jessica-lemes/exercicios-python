n1 = float(input("Digite o valor do primeiro produto: "))
n2 = float(input("Digite o valor do segundo produto: "))
n3 = float(input("Digite o valor do terceiro produto: "))

menor = 9999999999999999999999

if n1 < n2 and n1 < n3:
    menor = n1
    print("Você deve comprar o primeiro produto no valor de {0}".format(menor))
elif n2 < n1 and n2 < n3:
    menor = n2
    print("Você deve comprar o segundo produto no valor de {0}".format(menor))
elif n3 < n1 and n3 < n2:
    menor = n3
    print("Você deve comprar o terceiro produto no valor de {0}".format(menor))