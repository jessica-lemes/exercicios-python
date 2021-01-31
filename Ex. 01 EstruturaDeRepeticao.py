num = int(input("Informe uma nota de 0 a 10: "))

while num < 0 or num > 10:
    print("Número inválido")
    num = int(input("Informe um numero de 0 a 10: "))
print("A nota informada foi ", num)