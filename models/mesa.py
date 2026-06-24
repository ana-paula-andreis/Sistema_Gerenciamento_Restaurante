class Mesa:
    def __init__(self, numero, capacidade):
        self.numero = numero
        self.capacidade = capacidade
        self.ocupada = False
        #REGRA DE NEGÓCIO: UMA MESA PODE ESTAR OCUPADA OU LIVRE
        #SETADA SEMPRE COMO LIVRE AO SER CRIADA