lista = [2,3,4,5,6,7,8]

def encontra_impares(lista):
    if lista[0] % 2 == 0:
      del lista[0]
      encontra_impares(lista)
    else:
      return lista

encontra_impares(lista)