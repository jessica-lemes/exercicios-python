controle = True
def main(controle):
    while controle == True:
        num = int(input("Informe um número entre 0 e 16: "))
        if num < 0 or num > 16:
            controle = True
        else:
            controle = False
            contador = 1
            fat = 1
            while contador <= num:
                fat = fat * contador
                contador += 1
            print(fat)
            return recomecar()
            

def recomecar():
    controle = True

    recomeca = input("Deseja continuar? (S/N): ")
    if recomeca.upper() == "S":
        controle = True
        main(controle)
    elif recomeca.upper() == "N": 
        controle = False
        print("Volte sempre")
    else:
        print("Digite S ou N")
        recomecar()
    return controle
            
            
print(main(controle))