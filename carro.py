class Carro:
    def __init__(self):
        # inicializa as posições do carro no grid
        self.linha = 0
        self.coluna = 0
        # inicializa a direção do carro (N = norte, L = leste, S = sul, O = oeste)
        self.direcao = "N"
        # inicializa o histórico de movimentos do carro
        self.historico = []

    def virar_a_direita(self):
        # altera a direção do carro para a direita
        if self.direcao == "N":
            self.direcao = "L"
        elif self.direcao == "L":
            self.direcao = "S"
        elif self.direcao == "S":
            self.direcao = "O"
        else:
            self.direcao = "N"

    def virar_a_esquerda(self):
        # altera a direção do carro para a esquerda
        if self.direcao == "N":
            self.direcao = "O"
        elif self.direcao == "O":
            self.direcao = "S"
        elif self.direcao == "S":
            self.direcao = "L"
        else:
            self.direcao = "N"

    def mover(self):
        # move o carro na direção atual
        if self.direcao == "N":
            self.linha -= 1
        elif self.direcao == "L":
            self.coluna += 1
        elif self.direcao == "S":
            self.linha += 1
        else:
            self.coluna -= 1

        # adiciona o movimento atual ao histórico
        self.historico.append((self.linha, self.coluna, self.direcao))

    def get_posicao(self):
        # retorna a posição atual do carro
        return self.linha, self.coluna

    def get_direcao(self):
        # retorna a direção atual do carro
        return self.direcao

    def get_historico(self):
        # retorna o histórico de movimentos do carro
        return self.historico
