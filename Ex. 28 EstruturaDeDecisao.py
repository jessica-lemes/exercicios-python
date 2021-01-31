def inicio():
    carne = int(input("Informe o tipo de carne que deseja comprar: (1 para File Duplo, 2 para Alcatra e 3 para Picanha):  "))
    valor_carne = 0
    tipo_carne = ""  

    if carne < 0 or carne > 3:
         print("Informe uma opção válida")
         inicio()
    else:
        kg_carne = float(input("Informe quantos kilos deseja comprar: "))
        cartao_tabajara = int(input("Deseja pagar com cartão Tabajara? (1 para Sim ou 2 para Não): "))
        if cartao_tabajara > 2:
            print("Opção Inválida")
            inicio()
        
                
        if carne == 1:
            tipo_carne = "File Duplo"
            if kg_carne > 5:
                valor_carne = 5.80*kg_carne
            else:
                valor_carne = 4.90*kg_carne
            
        elif carne == 2:
            tipo_carne = "Alcatra"
            if kg_carne > 5:
                valor_carne = 6.80*kg_carne
            else:
                valor_carne = 5.90*kg_carne

        elif carne == 3:
            tipo_carne = "Picanha"
            if kg_carne > 5:
                valor_carne = 7.80*kg_carne
            else:
                valor_carne = 6.90*kg_carne
   

    meio_de_pagamento = meio_pagamento(valor_carne, cartao_tabajara)
    meio_de_pagamento

    return "Tipo de carne = {0}. Quantidade de KG = {1}Kg. Preço total = R${2:.2f}. Forma de pagamento = {3}. Desconto = {4:.2f}. Valor final = {5:.2f}. ".format(tipo_carne, kg_carne, valor_carne, meio_de_pagamento[0], meio_de_pagamento[1], meio_de_pagamento[2])

def meio_pagamento(valor_carne, cartao_tabajara):
    forma_pagamento = ""

    if cartao_tabajara == 1:
        pagamento = "Cartão Tabajara"
        desconto = valor_carne*0.05
        valor_final = valor_carne - desconto

    elif cartao_tabajara == 2:
        forma_pagamento = int(input("Informe o meio de pagamento: 1 para cartão de crédito, 2 para cartão de débito e 3 para dinheiro: "))
        if forma_pagamento > 3:
            return "Opção inválida"
            meio_pagamento(valor_carne, cartao_tabajara)
        else:
            if forma_pagamento == 1:
                pagamento = "Cartão de crédito"
            elif forma_pagamento == 2:
                pagamento = "Cartão de débito"
            elif forma_pagamento == 3:
                pagamento = "Dinheiro"

    desconto = 0.0
    valor_final = valor_carne

    return pagamento, desconto, valor_final
    
print(inicio())