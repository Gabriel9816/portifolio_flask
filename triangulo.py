class triangulo:
    def __init__(self):
        self.ladoA = 0
        self.ladoB = 0
        self.ladoC = 0

    def getPerimetro(self):
        return self.ladoA+self.ladoB+self.ladoC

    def getMaiorLado(self):
        return max(self.ladoA, self.ladoB, self.ladoC)

    def getArea(self):
        return self.ladoA*self.ladoB*self.ladoC


