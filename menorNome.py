def menor_nome(lista):
  nova_lista = []
  menor = 999
  for nome in lista:
    nome = nome.strip()
    nova_lista.append(nome)
    
  for nome in nova_lista:
    tam_nome = len(nome)
    
    while tam_nome < menor:
      resultado = nome
      menor = tam_nome
    
  return resultado.capitalize()