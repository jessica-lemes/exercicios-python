metros = float(input("Informe a area a ser pintada em metros: "))
valor_lata_tinta = 80

if metros >=3:
    qnt_litros = metros // 3 
    if metros % 3 != 0:
        qnt_litros = metros // 3 + 1

valor_total = qnt_litros * valor_lata_tinta

print("Você deverá comprar {0} lata(s) que custara(ão) R${1:.2f}".format(int(qnt_litros), valor_total))

