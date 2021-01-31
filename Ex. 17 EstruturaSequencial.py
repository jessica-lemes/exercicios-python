metros = float(input("Informe a area a ser pintada em metros: "))
litro_metro = 6.6

qnt_galao = 0
qnt_lata = 0

metros_lata = 18*litro_metro
metros_galao = 3.6*litro_metro

if metros <= metros_galao:
    print("Você deverá comprar um galão de 3 litros")

elif metros <= metros_lata and metros > metros_galao:
    if metros % metros_galao != 0:
        qnt_galao = metros // metros_galao + 1
    else:
        qnt_galao =  metros // metros_galao
    print("Você deverá comprar {0} galão(ões) de 3 litros".format(int(qnt_galao)))

elif metros >= metros_lata:
    qnt_lata = metros // metros_lata
    resto = metros % metros_lata 
    if metros % metros_lata != 0:
        if resto != 0:
            qnt_galao = resto // metros_galao + 1
        else:
            qnt_galao = resto // metros_galao
    print("Você deverá comprar {0} galão(ões) de 3 litros e {1} lata(s) de 18 litros".format(int(qnt_galao),int(qnt_lata)))
