n = int(input("Digite um número menor que 1000: "))


def calcula_centena_dezena_unidade(n):
    centena = n // 100
    resto_centena = n % 100
    dezena = resto_centena // 10
    unidade = resto_centena % 10

    if centena > 1:
        palavra_centena = "centenas"
    else:
        palavra_centena = "centena"
    if dezena > 1:
        palavra_dezena = "dezenas"
    else:
        palavra_dezena = "dezena"
    if unidade > 1:
        palavra_unidade = "unidades"
    else:
        palavra_unidade = "unidade"

    return "{0} = {1} {2}, {3} {4} e {5} {6}".format(n, centena,palavra_centena, dezena,palavra_dezena, unidade, palavra_unidade)


while n > 1000:
    print("Número informado inválido")
    n = int(input("Digite um número menor que 1000: "))
print(calcula_centena_dezena_unidade(n))