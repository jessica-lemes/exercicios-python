'''Faça um Programa que peça dois números e imprima a soma.'''


def somador():
    num1 = float(input("Informe um número: "))
    num2 = float(input("Informe mais um número: "))
    soma = num1 + num2
    return "A soma destes números é: {0}".format(soma)

print(somador())