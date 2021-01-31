def calcula_frutas():
    
    kg_maca = float(input("Informe a quantidade de maca que deseja comprar: "))
    kg_morango = float(input("Informe a quantidade de morango que deseja comprar: "))

    if kg_maca < 0 or kg_morango < 0:
        print("Kg nao pode ser menor que zero")
        return calcula_frutas()
    else:
        if kg_maca > 0 and kg_maca < 5:
            maca = 1.80
        elif kg_maca > 5:
            maca = 1.50
        if kg_morango > 0 and kg_morango < 5:
            morango = 2.50
        elif kg_morango > 5:
            morango = 2.20
        
    total_maca = maca*kg_maca
    total_morango = morango*kg_morango
    total_frutas = total_maca + total_morango

    if total_frutas > 8:
        desconto = total_frutas*0.10
        valor_final = total_frutas  - desconto
    
    return "{0} kg de maça + {1} kg de morango totalizam {2:.2f} reais.".format(kg_maca,kg_morango,valor_final)

print(calcula_frutas())