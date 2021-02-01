'''Faça um Programa que peça um número e então mostre a mensagem O número informado foi [número].'''

def numero():
    num = int(input("Informe um número: "))
    return "O número informado foi: {0} ".format(num)

print(numero())