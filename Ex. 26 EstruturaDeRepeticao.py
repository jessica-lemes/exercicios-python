'''Numa eleição existem três candidatos.
Faça um programa que peça o número total de eleitores. Peça para cada eleitor votar e ao final mostrar o número de votos de cada candidato.'''

eleitores = int(input("Informe quantos eleitores irão votar: "))
candidato = 0
candidatoUm = 0
candidatoDois = 0
candidatoTres = 0
nulo = 0
contador = 0
while contador < eleitores:
    candidato = int(input("Informe o numero do seu candidato: "))
    if candidato == 1:
        candidatoUm += 1
    elif candidato == 2:
        candidatoDois += 1
    elif candidato == 3:
        candidatoTres += 1
    else:
        nulo += 1
    contador += 1

print("O candidato 1 recebeu {0} voto(s). O candidato 2 recebeu {1} voto(s). O candidato 3 recebeu {2} voto(s). E {3} eleitores votaram nulo.".format(candidatoUm, candidatoDois, candidatoTres, nulo))