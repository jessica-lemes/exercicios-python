def inicio():
    print("Conversão de criptomoedas")
    print("1 - Converter Bitcoin em reais")
    print("2 - Converter reais em Bitcoin ")
    print("3 - Sair")

    controle = int(input("Escolha uma opção: "))

    if (controle == 3):
        print("Obrigado por utilizar a calculadora de Bitcoin. Volte sempre.")

    if (controle == 1):
        num1 = float(input("Digite um valor em Bitcoin: "))
        num2 = float(input("Digite a cotação atual: "))

        valor = num1*num2

        print(num1,"bitcoin equivale a ", valor, "reais")
        inicio()

    if (controle == 2):
        num1 = float(input("Digite um valor em reais: "))
        num2 = float(input("Digite a cotação atual: "))

        valor = num1/num2

        print(num1,"reais equivale a ", valor, "bitcoins")
        inicio()

inicio()