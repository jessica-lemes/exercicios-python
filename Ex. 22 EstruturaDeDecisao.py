numero = float(input("Informe um número: "))

def verificaPar(numero):
    if int(numero) % 2 == 0:
        return "Par"
    else:
        return "Ímpar"
    
def verificaDecimal(numero):
    if numero % 1 == 0:
        return verificaPar(numero)
    else:
        return "Este número não pode ser classificado"

print(verificaDecimal(numero))