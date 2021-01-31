'''Faça um programa que calcule o mostre a média aritmética de N notas.'''

qnt_notas = int(input("Informe quantas notas deseja inserir: "))
contador = 1
soma = 0
while contador <= qnt_notas:
    nota = float(input("Informe a nota: "))
    contador += 1
    soma += nota
    media = soma / qnt_notas
print(media)

