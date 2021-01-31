n1 = float(input("Digite o primeiro número: "))
n2 = float(input("Digite o segundo número: "))
n3 = float(input("Digite o terceiro número: "))

maior = 0

if n1 > n2 and n1 > n3:
    maior = n1
    print("O número {0} é o maior".format(maior))
elif n2 > n1 and n2 > n3:
    maior = n2
    print("O número {0} é o maior".format(maior))
elif n3 > n1 and n3 > n2:
    maior = n3
    print("O número {0} é o maior".format(maior))
