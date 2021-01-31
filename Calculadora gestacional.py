from datetime import datetime,date

def inicio():
    print("Calculadora gestacional")
    print("Informe a data da sua ultima menstruação")
    dia = int(input("Informe o dia: "))
    mes = int(input("Informe o mês: "))
    ano = int(input("Informe o ano: "))
    
    return valida(dia,mes,ano)

def valida(dia, mes , ano):
    if dia > 31 or dia < 0:
        print("Dia informado inválido. Digite novamente")
        inicio()
    elif mes > 12 or mes < 0:
        print("Mes informado inválido. Digite novamente")
        inicio()
    elif ano < 10 or len(str(ano)) != 2:
        print("Ano informado inválido. Digite novamente")
        inicio()
    else:
        return dia, mes, ano

def calc_dpp(dia, mes , ano):
    if mes > 3:
        mes -= 3
        ano += 1
    else:
        mes += 9

    if dia > 23:
        dia -= 23
        mes += 1
    else:
        dia += 7
    
    return dia,mes,ano

def calc_semanas(dia,mes,ano):
    dum_informada = "{2}-{1}-{0}".format(dia,mes,ano)
    dum = datetime.strptime(dum_informada,'%y-%m-%d')
    data_atual = datetime.today()
    id_gest_dias = abs((dum - data_atual).days)
    ig_semanas = id_gest_dias // 7
    if id_gest_dias % 7 !=0:
        ig_dias = id_gest_dias % 7 - 1
    else:
        ig_dias = 0
    
    return "Idade gestacional: {0:.0f} semanas e {1:.0f} dias".format(ig_semanas,ig_dias)

inicia_programa = inicio()
dpp = calc_dpp(inicia_programa[0],inicia_programa[1],inicia_programa[2])
idade_gestacional = calc_semanas(inicia_programa[0],inicia_programa[1],inicia_programa[2])
print("A data provável do parto será {0}/{1}/{2}".format(dpp[0],dpp[1],dpp[2]))
print(idade_gestacional)