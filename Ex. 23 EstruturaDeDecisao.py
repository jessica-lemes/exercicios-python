numero = float(input("Informe um número: "))

def verificaDecimal(numero):
    if numero % 1 == 0:
        return "Inteiro"
    else:
        return "Decimal"

print(verificaDecimal(numero))