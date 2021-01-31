num1 = float(input("Informe o primeiro número: "))
num2 = float(input("Informe o segundo número: "))

print("Escolha entre as opções abaixo: ")
print("** 1 para par ou ímpar **")
print("** 2 para positivo ou negativo **")
print("** 3 para inteiro ou decimal **")

operacao = int(input("Informe a operação que deseja realizar: "))

if operacao == 1:
    if num1 % 1 == 0:
        if num1 % 2 == 0:
            print("O primeiro número é Par")
        else:
            print("O primeiro número é Ímpar")
    else:
        print("O primeiro número não pode ser classificado")
    
    if num2 % 1 == 0:
        if num2 % 2 == 0:
            print("O segundo número é Par")
        else:
            print("O segundo número é Ímpar")
    else:
        print("O segundo número não pode ser classificado")
    
elif operacao == 2:
    if num1 < 0:
        print("O primeiro número é Negativo")
    else:
        print("O primeiro número é Positivo")
    if num2 < 0:
        print("O segundo número é Negativo")
    else:
        print("O segundo número é Positivo")

elif operacao == 3:
    if num1 % 1 == 0:
        print("O primeiro número é Inteiro")
    else:
        print("O primeiro número é Decimal")
    if num2 % 1 == 0:
        print("O segundo número é Inteiro")
    else:
        print("O segundo número é Decimal")