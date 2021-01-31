num_dia_semana = int(input("Digite um número: "))

if num_dia_semana == 1:
    dia_semana = "Domingo"
elif num_dia_semana == 2:
    dia_semana = "Segunda-feira"
elif num_dia_semana == 3:
    dia_semana = "Terça-feira"
elif num_dia_semana == 4:
    dia_semana = "Quarta-feira"
elif num_dia_semana == 5:
    dia_semana = "Quinta-feira"
elif num_dia_semana == 6:
    dia_semana = "Sexta-feira"
elif num_dia_semana == 7:
    dia_semana = "Sábado"
else:
    print("Número inválido")

print(dia_semana)