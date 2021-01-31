periodo = input("Qual o período que você estuda? (M-Matutino, V-Vespertino, N-Noturno): ")

if periodo.upper() == "M":
    print("Bom dia")
elif periodo.upper() == "V":
    print("Boa tarde")
elif periodo.upper() == "N":
    print("Boa noite")  
else:
    print("Período inválido")  