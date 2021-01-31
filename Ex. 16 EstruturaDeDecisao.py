import math

a = int(input("Digite o valor de a: "))
b = int(input("Digite o valor de b: "))
c = int(input("Digite o valor de c: "))

def valida_equacao(a,b,c):
    if a <= 0:
        return "Esta não é uma equação de segundo grau"
    else:
        return delta(a,b,c)

def delta(a,b,c):
    delta = ((b*b) - 4*a*c)
    if delta > 0:
        return delta, raizes(delta,a,b,c)
    elif delta == 0:
        return "Possui apenas uma raíz real" , delta
    else:
        return "Não existem raizes reais"

def raizes(delta,a,b,c):
    x1 = (-b + math.sqrt(delta))/(2*a)
    x2 = (-b - math.sqrt(delta))/(2*a)
    return ("Raiz 1 = {0} , Raiz 2 = {1}".format(x1, x2))

inicio = valida_equacao(a,b,c)
print(inicio)