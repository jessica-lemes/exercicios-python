letra = input("Digite uma letra: ")

if letra.upper() == 'A' or letra.upper() == 'E' or letra.upper() == 'I' or letra.upper() == 'O' or letra.upper() == 'U':
    print("{0} é vogal".format(letra))
else:
    print("{0} é consoante".format(letra))
