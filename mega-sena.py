from random import sample

quantidade = int(input("Digite a quantidade de números para mega-sena: "))

sorteados = sample(range(1,61), quantidade)

sorteados.sort()

print(sorteados)