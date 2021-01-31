nome = input("Informe o nome: ")
while len(nome) <= 3:
    print("O nome precisa ter mais que 3 caracteres")
    nome = input("Informe o nome: ")
nome = nome

idade = int(input("Informe a idade: "))
while idade < 0 or idade > 150:
    print("Informe uma idade entre 0 e 150 anos")
    idade = int(input("Informe a idade: "))
idade = idade

salario = float(input("Informe o salário: "))
while salario <= 0:
    print("Informe um salario maior do que R$ 0.0 ")
    salario = input("Informe o salário: ")
salario = salario

sexo = input("Informe o sexo (F ou M): ")
while sexo.lower() != "f" and sexo.lower() != "m":
    print("Informação inválida, digite F para feminino ou M para masculino")
    sexo = str(input("Informe o sexo (F ou M): "))
sexo = sexo

estado_civil = input("Informe o estado civil (S para solteiro, C para casado, V para viuvo, D para divorciado): ")
while estado_civil.lower() != "s" and estado_civil.lower() != "c" and estado_civil.lower() != "v" and estado_civil.lower() != "d":
    print("Informação inválida")
    estado_civil = input("Informe o estado civil (S para solteiro, C para casado, V para viuvo, D para divorciado): ")
estado_civil = estado_civil

print(nome, idade,salario, sexo, estado_civil)