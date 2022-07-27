class Classes:
    def __init__(self, v, i):
        self.valor = v
        self.incremento = i
        self.decremento = i
        self.multiplicar = v

    def calc_incremento(self):
        self.valor = self.valor + self.incremento

    def calc_decremento(self):
        self.valor = self.valor - self.decremento

    def calc_multiplicar(self, m=2):
        self.multiplicar = self.valor * m

print('- Descubra o valor do incremento -')
x = Classes(float(input('Digite um valor: ')), float(input('Digite um incremento: ')))
x.calc_incremento()
print(x.valor)

print('- Descubra o valor do decremento -')
y = Classes(float(input('Digite um valor: ')), float(input('Digite um decremento: ')))
y.calc_decremento()
print(y.valor)

z = Classes(x.valor, y.valor)
z.calc_multiplicar()
print(f'A multiplicação é {z.multiplicar}')

