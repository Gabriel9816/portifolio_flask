class Triangulo:
    def __init__(self, ladoA: int, ladoB: int, ladoC: int) -> None:
        if ((ladoA + ladoB) > ladoC) and ((ladoA + ladoC) > ladoB) and ((ladoB + ladoC) > ladoA):
            self.a_lado = ladoA
            self.b_lado = ladoB
            self.c_lado = ladoC
            self.type = self._type()
        else:
            raise Exception("Os lados não formam triangulo")

    def _type(self) -> str:
        sides = set((self.a_lado, self.b_lado, self.c_lado))
        if len(sides) == 1:
            return 'Equilatero'
        if len(sides) == 2:
            return 'Isosceles'
        if len(sides) == 3:
            return 'Escaleno'

    def get_perimetro(self) -> int:
        return self.a_lado + self.b_lado + self.c_lado

    def get_lado_maior(self) -> int:
        return self
