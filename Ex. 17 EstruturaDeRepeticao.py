num = int(input("Informe o número que deseja que seja calculado seu fatorial: "))
contador = 1
fat = 1
while contador <= num:
    fat = fat * contador
    contador += 1
print(fat)