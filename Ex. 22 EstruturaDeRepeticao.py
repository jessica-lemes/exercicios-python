#Altere o programa de cálculo dos números primos, informando, caso o número não seja primo, por quais número ele é divisível.

num = int(input("Informe um número inteiro: "))
contador = 1
divisor = 0
lista = []
while contador <= num:
    if num % contador == 0:
        divisor += 1
        lista.append(contador)
    contador += 1

if divisor > 2:
    print("Não é primo")
    print("Este número é divisível por: ", lista)
else:
    print("Primo")
