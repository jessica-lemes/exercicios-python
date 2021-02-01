'''Faça um programa que calcule o valor total investido por um colecionador em sua coleção de CDs e o valor 
médio gasto em cada um deles. O usuário deverá informar a quantidade de CDs e o valor para em cada um.'''

qntCds = int(input("Informe a quantidade de CDs: "))
contador = 1
soma = 0

while contador <= qntCds:

    valor = float(input("Informe o valor gasto no CD " +str(contador)+ ": "))
    soma += valor
    contador += 1

media = soma / qntCds


print("A média gasta em cada CD foi de R$", media, "E o valor total investido foi de R$", soma)