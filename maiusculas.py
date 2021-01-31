def  maiusculas(frase):
  maiuscula = ""
  for letra in frase:
    if ord(letra) > 65 and ord(letra) < 95:
      maiuscula += letra
  return maiuscula