class Triangulo:
  def __init__(self, a, b, c):
    self.a = a
    self.b = b
    self.c = c

  def perimetro(self):
    soma = self.a +self.b + self.c
    return soma

  def tipo_lado(self):
    
    if self.a == self.b and self.c == self.a:
      return "equilátero"
    elif self.a == self.b or self.b==self.c or self.a == self.c:
      return "isósceles"
    else:
      return "escaleno"
