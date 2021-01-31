valor_hora = float(input("Informe seu salario/hora: "))
horas_trabalhadas = float(input("Informe as horas trabalhadas no mês: "))

salario_bruto = valor_hora * horas_trabalhadas
inss = salario_bruto * 0.10
fgts = salario_bruto * 0.11


def desconto_ir(salario_bruto):
    if salario_bruto < 900:
        desconto = 0
        porc_ir = 0
    elif salario_bruto < 1500:
        desconto = salario_bruto * 0.05
        porc_ir = 5
    elif salario_bruto < 2500:
        desconto = salario_bruto * 0.10
        porc_ir = 10
    elif salario_bruto >= 2500:
        desconto = salario_bruto * 0.20
        porc_ir = 20
    return porc_ir, desconto

ir = desconto_ir(salario_bruto)

total_descontos = inss+ir[1]
salario_liquido = salario_bruto - total_descontos

print("Salario Bruto: ({0:.2f} * {1:.2f})\t: R${2:.2f} \n(-)IR({3:.2f}%)\t\t\t: R${4:.2f}\n(-)INSS(10%)\t\t\t: R${5:.2f}\nFGTS(11%)\t\t\t: R${6:.2f}\nTotal de descontos\t\t: R${7:.2f}\nSalário Liquido\t\t\t: R${8:.2f}".format(valor_hora, horas_trabalhadas, salario_bruto,ir[0],ir[1],inss, fgts, total_descontos, salario_liquido))