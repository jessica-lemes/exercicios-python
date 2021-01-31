n1 = float(input("Digite o primeiro número: "))
n2 = float(input("Digite o segundo número: "))
n3 = float(input("Digite o terceiro número: "))

menor = 9999999999999999999999

if n1 < n2 and n1 < n3:
    menor = n1
    print("O número {0} foi o menor número informado".format(menor))
elif n2 < n1 and n2 < n3:
    menor = n2
    print("O número {0} foi o menor número informado".format(menor))
elif n3 < n1 and n3 < n2:
    menor = n3
    print("O número {0} foi o menor número informado".format(menor))