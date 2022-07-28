class PrecoCarro:
    def __init__(self, preco, ano):
        self.preco = preco
        self.ano = ano

    def desconto(self, percent):
        percent = (int(input('Insira o valor do desconto: ')))
        self.preco = self.preco - (self.preco * (percent / 100))

#getter preço
    @property
    def preco(self):
        return self._preco

#setter preço
    @preco.setter
    def preco(self, price):
        self._preco = price
        if self.preco >= 70000:
            print('Valores acima de 75k tem desconto')
            print(self.desconto(0))

#getter ano
    @property
    def ano(self):
        return self._ano

#setter ano
    @ano.setter
    def ano(self, year):
        self._ano = year
        if self.ano >= 2020:
            print('Carro acima de 2020 tem desconto')
            print(self.desconto(0))


carroA = PrecoCarro(int(input('Insira o valor do veículo: ')), int(input('Insira o ano: ')))

carroB = PrecoCarro(int(input('Insira o valor do veículo: ')), int(input('Insira o ano: ')))

print(f'Valor do carro A, do ano de {carroA.ano}, é R$ {carroA.preco}.')
print(f'Valor do carro B, do ano de {carroB.ano}, é R$ {carroB.preco}.')
