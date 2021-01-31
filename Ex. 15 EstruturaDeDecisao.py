lado1 = float(input("Informe o tamanho do primeiro lado em cm: "))
lado2 = float(input("Informe o tamanho do segundo lado em cm: "))
lado3 = float(input("Informe o tamanho do terceiro lado em cm: "))

def valida_triangulo(lado1,lado2,lado3):
    if lado1 > 0 or lado2 > 0 or lado3 > 0:
        if lado1 + lado2 > lado3:
            triangulo = True
        elif lado1 + lado3 > lado2:
            triangulo = True
        elif lado2 + lado3 > lado1:
            triangulo = True
        else:
            triangulo = False
    else:
        triangulo = False

    if triangulo == True:
        return "É triângulo" , define_triangulo(lado1,lado2,lado3)
    else:
        return "Não é triângulo"

def define_triangulo(lado1,lado2,lado3):
    if lado1 == lado2 and lado1 == lado3:
        tipo_triangulo = "Equilátero"
    elif lado1 == lado2 or lado1 == lado3 or lado2 == lado3:
        tipo_triangulo = "Isósceles"
    elif  lado1 != lado2 and lado1 != lado3 and lado2 != lado3:
        tipo_triangulo = "Escaleno"
    return tipo_triangulo

valida_triangulo = valida_triangulo(lado1,lado2,lado3)

print(valida_triangulo)