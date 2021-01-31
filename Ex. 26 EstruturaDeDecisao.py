def inicio():
    qnt_combustivel = float(input("Informe a quantidade de combutível a ser abastecido: "))
    combustivel = input("Informe o tipo de combustível: (A para Alcool e G para Gasolina)  ")

    if combustivel.upper() == "A":
        a = calcula_alcool(qnt_combustivel)
        resultado = "O valor total a ser pago será: R$ " + str(round(a,2)) 
    elif combustivel.upper() == "G":
        g =  calcula_gasolina(qnt_combustivel)
        resultado = "O valor total a ser pago será: R$ " + str(round(g,2)) 
    else:
        print("Informe uma opção válida")
        return inicio()

    return resultado

def calcula_alcool(qnt_combustivel):
    alcool = 1.90
    if qnt_combustivel < 20.0:
        valor = qnt_combustivel*alcool
        desconto = valor * 0.03
        total = valor - desconto

    elif qnt_combustivel > 20.0:
        valor = qnt_combustivel*alcool
        desconto = valor * 0.05
        total = valor - desconto

    return total


def calcula_gasolina(qnt_combustivel):
    gasolina = 2.50
    if qnt_combustivel < 20.0:
        valor = qnt_combustivel*gasolina
        desconto = valor * 0.04
        total = valor - desconto

    elif qnt_combustivel > 20.0:
        valor = qnt_combustivel*gasolina
        desconto = valor * 0.06
        total = valor - desconto

    return total

print(inicio())