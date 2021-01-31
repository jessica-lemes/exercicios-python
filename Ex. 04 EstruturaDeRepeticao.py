pais_a = 80000
pais_b = 200000

taxa_pais_a = 3
taxa_pais_b = 1.5

ano = 0

while pais_a < pais_b:
    ano = ano + 1
    pais_b = pais_b + (pais_b*0.015)
    pais_a = pais_a + (pais_a*0.03)
    
print("O país A levou {0} anos para alcançar o número de habitantes do país B".format(ano))