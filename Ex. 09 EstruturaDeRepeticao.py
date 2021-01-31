def devolve_impares():
    num = 0
    numeros = []
    while num <= 50:
        if num % 2 != 0:
            numeros.append(num)

        num += 1
            
    return numeros

print(devolve_impares())