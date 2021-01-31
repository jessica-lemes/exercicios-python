base = int(input("Informe o valor da base: "))
expoente = int(input("Informe o valor do expoente: "))

contagem = 0
resultado = base
while contagem < (expoente-1):
    contagem += 1
    resultado = resultado * base
print(resultado)