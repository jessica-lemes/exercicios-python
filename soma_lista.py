def soma_lista(lista):
  if len(lista) == 1:
    return lista[0]
  else:
    lista[0] = lista[0]+lista[1]
    del lista[1]
    return soma_lista(lista)