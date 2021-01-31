def inicio():
    saque = int(input("Informe um valor para saque: "))
    print(saque)
    if saque < 10:
        print("Valor mínimo para saque = 10 reais")
        return inicio()
    elif saque > 600:
        print("Valor máximo para saque = 600 reais")
        return inicio()
    elif saque >= 10 and saque < 600:
        return calcula_notas(saque)

def resposta(calcula_notas):
    resp = "Você receberá: "
    if calcula_notas[0] > 0:
       resp += str(calcula_notas[0])+ " nota(s) de R$100 "
    if calcula_notas[1] > 0:
       resp += str(calcula_notas[1])+ " nota(s) de R$50 "
    if calcula_notas[2] > 0:
       resp += str(calcula_notas[2])+ " nota(s) de R$10 "
    if calcula_notas[3] > 0:
       resp += str(calcula_notas[3])+ " nota(s) de R$5 "
    if calcula_notas[4] > 0:
       resp += str(calcula_notas[4])+ " nota(s) de R$1." 

    return resp

def calcula_notas(saque):
    notas_cem  = saque // 100
    resto_cem = saque % 100
  
    notas_cinquenta = resto_cem // 50
    resto_cinquenta = resto_cem % 50

    notas_dez = resto_cinquenta // 10
    resto_dez = resto_cinquenta % 10

    notas_cinco = resto_dez // 5
    resto_cinco = resto_dez % 5

    notas_um = resto_cinco // 1
    resto_um = resto_cinco % 1

    calcula_notas = notas_cem, notas_cinquenta, notas_dez, notas_cinco, notas_um
    return resposta(calcula_notas)
    
print(inicio())