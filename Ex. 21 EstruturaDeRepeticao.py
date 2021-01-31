'''Faça um programa que peça um número inteiro e determine se ele é ou não um número primo.
Um número primo é aquele que é divisível somente por ele mesmo e por 1.'''

num = int(input("Informe um número inteiro: "))
contador = 1
divisor = 0

while contador <= num:
    if num % contador == 0:
        divisor += 1
    contador += 1

if divisor > 2:
    print("Não é primo")
else:
    print("Primo")
