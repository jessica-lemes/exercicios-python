def valida_dia(dia,mes,ano):

    if (ano % 4 == 0 and ano % 100 != 0) or (ano % 400 == 0):
        ano_bissexto = True
    else:
        ano_bissexto = False

    if dia > 0:
        if ano_bissexto == True:
            if mes == 2:
                if dia > 0 and dia <= 29:
                    dia = True
            else:
                dia = False
        else:
            if mes == 1 or mes == 3 or mes == 5 or mes == 7 or mes == 8 or mes == 10 or mes == 12:
                if dia > 0 and dia <= 31:
                    dia = True
            elif mes == 4 or mes == 6 or mes == 9 or mes == 11:
                if dia > 0 and dia <= 30:
                    dia = True
            else:
                dia = False 
    return dia

def valida_mes(mes):
    if mes < 0 or mes > 12:
        mes = False
    else:
        mes = True
    return mes

def valida_ano(ano):
    if ano < 0:
        ano = False
    else:
        ano = True
    return ano

def inicio():
    print('='*18)
    print("Valida data")
    print('='*18)

    data = input("Informe a data: ")

    dia, mes, ano = data.split("/")
    dia = int(dia)
    mes = int(mes)
    ano = int(ano)
    
    dia_validado = valida_dia(dia,mes,ano)
    mes_validado = valida_mes(mes)
    ano_validado = valida_ano(ano)


    if dia_validado == True and mes_validado == True and ano_validado == True:
        resultado = "A data "  + data + " é válida"
    else:
        resultado = "A data " + data + " não é válida"

    return resultado

print(inicio())