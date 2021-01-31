def inicio():

    pais_a = int(input("Informe a quantidade de habitantes do país A: "))
    pais_b = int(input("Informe a quantidade de habitantes do país B: "))

    taxa_pais_a = float(input("Informe a taxa de crescimento anual do país A: "))
    taxa_pais_b = float(input("Informe a taxa de crescimento anual do país B: "))

    tx_a_em_porc = taxa_pais_a / 100
    tx_b_em_porc = taxa_pais_b / 100

    ano = 0
    while pais_a < pais_b:
        ano = ano + 1
        pais_b = pais_b + (pais_b*tx_b_em_porc)
        pais_a = pais_a + (pais_a*tx_a_em_porc)
        
    print("O país A levou {0} anos para alcançar o número de habitantes do país B".format(ano))

    return deseja_continuar()


def deseja_continuar():
    continuar = input("Deseja fazer uma nova pesquisa? (S/N)")
    if continuar.upper() == "S":
        inicio()
    elif continuar.upper() == "N":
        print("Obrigado e volte sempre!!")
    else:
        print("Resposta inválida. Informe S ou N")
        return deseja_continuar()
     
print(inicio())