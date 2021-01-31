nome = input("Informe o nome: ")
senha = input("Informe a senha: ")

while senha == nome:
    print("A senha não pode ser igual ao nome de usuário!")
    nome = input("Informe o nome: ")
    senha = input("Informe a senha: ")
print("Seja bem vindo(a)", nome)