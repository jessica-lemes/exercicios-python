s1 = float(input("Informe a nota do primeiro semestre: "))
s2 = float(input("Informe a nota do segundo semestre: "))

media = (s1+s2) / 2

if media >= 9.0:
    conceito = "A"
    res_final = "Aprovado"
elif media >= 7.5 < 9.0:
    conceito = "B"
    res_final = "Aprovado"
elif media >= 6.0 < 7.5:
    conceito = "C"
    res_final = "Aprovado"
elif media > 4.0 < 6.0:
    conceito = "D"
    res_final = "Reprovado"
elif media < 4.0:
    conceito = "E"
    res_final = "Reprovado"

print("Sua nota final: {0} , seu conceito: {1}. Você foi {2}" .format(media,conceito,res_final))