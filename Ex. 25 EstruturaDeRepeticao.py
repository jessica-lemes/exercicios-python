'''Faça um programa que peça para n pessoas a sua idade, ao final o programa devera verificar se a média de idade da turma varia entre 0 e 25,
26 e 60 e maior que 60; e então, dizer se a turma é jovem, adulta ou idosa, conforme a média calculada.'''

idade = -1
jovem = 0
adulta = 0
idosa = 0
while idade != 0:
    idade = int(input("Informe a idade: (Digite 0 para sair)  "))
    if idade != 0 and idade <= 25:
        jovem += 1
    elif idade > 25 and idade <= 60:
        adulta +=1
    elif idade > 60:
        idosa += 1
    
total = jovem + adulta + idosa
media = total // 3
print(jovem, adulta, idosa)

if jovem > adulta and jovem > idosa and jovem > media:
    print("Turma jovem")
elif adulta > jovem and adulta > idosa and adulta > media:
    print("Turma adulta")
elif idosa > adulta and idosa > jovem and idosa > media:
    print("Turma idosa")

