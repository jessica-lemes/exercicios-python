sexo = input("Informe o sexo (M/F): ")

if sexo.upper() == "F":
    resposta = "feminino"
elif sexo.upper() == "M":
    resposta = "masculino"
else:
    resposta = "sexo inválido"

print(resposta)