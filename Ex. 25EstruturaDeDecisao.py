print("Responda as 5 questões para saber sobre a participação da pessoa no crime.")

def telefonou():
    resposta = input("Telefonou para a vítima? S/N:  ")
    if resposta.upper() == "S":
        seTelefonou = True
        return seTelefonou
    elif resposta.upper() == "N":
        seTelefonou = False
        return seTelefonou
    else:
        print("Opção inválida")
        return telefonou()

def local():
    resposta = input("Esteve no local do crime? S/N:  ")
    if resposta.upper() == "S":
        esteve = True
        return esteve
    elif resposta.upper() == "N":
        esteve = False
        return esteve
    else:
        print("Opção inválida")
        return local()

def moraPerto():
    resposta = input("Mora perto da vítima? S/N:  ")
    if resposta.upper() == "S":
        mora = True
        return mora
    elif resposta.upper() == "N":
        mora = False
        return mora
    else:
        print("Opção inválida")
        return moraPerto()

def divida():
    resposta = input("Devia para a vítima? S/N:  ")
    if resposta.upper() == "S":
        devia = True
        return devia
    elif resposta.upper() == "N":
        devia = False
        return devia
    else:
        print("Opção inválida")
        return divida()

def trabalhou():
    resposta = input("Devia para a vítima? S/N:  ")
    if resposta.upper() == "S":
        seTrabalhou = True
        return seTrabalhou
    elif resposta.upper() == "N":
        seTrabalhou = False
        return seTrabalhou
    else:
        print("Opção inválida")
        return trabalhou()

def classifica():
    resposta1 = telefonou()
    resposta2 = local()
    resposta3 = moraPerto()
    resposta4 = divida()
    resposta5 = trabalhou()

    respostas = []
    respostas.append(resposta1)
    respostas.append(resposta2)
    respostas.append(resposta3)
    respostas.append(resposta4)
    respostas.append(resposta5)

    verdadeiro = 0
    for resposta in respostas:  
        if resposta == True:
            verdadeiro +=1
    if verdadeiro == 2:
        return "Suspeito"
    elif verdadeiro == 3 or verdadeiro == 4:
        return "Cumplice"
    elif verdadeiro == 5:
        return "Assassino"
    else:
        return "Inocente"

print(classifica())