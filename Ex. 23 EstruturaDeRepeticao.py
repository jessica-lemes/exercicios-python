"""Faça um programa que mostre todos os primos entre 1 e N sendo N um número inteiro fornecido pelo usuário. 
O programa deverá mostrar também o número de divisões que ele executou para encontrar os números primos."""

num = int(input("Informe um número inteiro: "))

numAtual = 1
primos = []

while numAtual <= num:
    contador = 1    
    divisor = 0

    while contador <= numAtual:
        if numAtual % contador == 0:
            divisor += 1
        contador += 1

    if divisor <= 2:
        primos.append(numAtual)
    
    numAtual += 1

print(primos)



