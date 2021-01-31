count = 0
pares = 0
impares = 0

while count < 10:
    numero = int(input("Informe um número inteiro: "))
    count += 1
    if numero % 2 == 0:
        pares += 1
    else:
        impares += 1
print("O total de números pares é: ", pares," e números ímpares: ", impares)

