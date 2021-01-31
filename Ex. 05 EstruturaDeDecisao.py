n1 = float(input("Digite a primeira nota: "))
n2 = float(input("Digite a segunda nota: "))

media = (n1 + n2) / 2
print(media)
if media >= 10:
    print("Aprovado com distinção")
elif media >= 7:
    print("Aprovado")
else:
    print("Reprovado")