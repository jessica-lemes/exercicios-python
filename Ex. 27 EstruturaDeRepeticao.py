'''Faça um programa que calcule o número médio de alunos por turma.
Para isto, peça a quantidade de turmas e a quantidade de alunos para cada turma. As turmas não podem ter mais de 40 alunos.'''

qntTurmas = int(input("Informe a quantidade de turmas: "))
contador = 1
soma = 0

while contador <= qntTurmas:
    alunos = int(input("Informe a quantidade de alunos da turma {0}. (Maximo de 40 alunos): ".format(contador)))
    if alunos <= 40:
        soma += alunos
        contador += 1

media = soma / qntTurmas


print("A media de alunos por turma é de", media, "alunos.")

