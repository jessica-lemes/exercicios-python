#até 280 = 20%
#de 280 a 700 = 15%
#700 a 1500 = 10%
#acima de 1500 = 5%

"""Após o aumento ser realizado, informe na tela:
o salário antes do reajuste;
o percentual de aumento aplicado;
o valor do aumento;
o novo salário, após o aumento."""

salario = float(input("Informe seu salário: "))

if salario <= 280:
    novo_salario = salario + salario * 0.20
    aumento = novo_salario - salario
    print("Seu salário de {0} recebeu aumento de {1} que equivale a 20% do seu valor atual, resultando em um novo salário de {2}".format(salario,aumento,novo_salario))

if salario > 280 and salario <= 750:
    novo_salario = salario + salario * 0.15
    aumento = novo_salario - salario
    print("Seu salário de {0} recebeu aumento de {1} que equivale a 30% do seu valor atual, resultando em um novo salário de {2}.".format(salario,aumento,novo_salario))

if salario > 750 and salario < 1500:
    novo_salario = salario + salario * 0.10
    aumento = novo_salario - salario
    print("Seu salário de {0} recebeu aumento de {1} que equivale a 10% do seu valor atual, resultando em um novo salário de {2}.".format(salario,aumento,novo_salario))

if salario >= 1500:
    novo_salario = salario + salario * 0.05
    aumento = novo_salario - salario
    print("Seu salário de {0} recebeu aumento de {1} que equivale a 5% do seu valor atual, resultando em um novo salário de {2}.".format(salario,aumento,novo_salario))