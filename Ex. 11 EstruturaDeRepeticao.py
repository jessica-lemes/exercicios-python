num1 = int(input("Informe o primeiro número: "))
num2 = int(input("Informe o último número: "))
soma = 0

while num1 < (num2-1):
    num1 += 1
    soma += num1 
    print(num1)
print("números somados: ",soma)
