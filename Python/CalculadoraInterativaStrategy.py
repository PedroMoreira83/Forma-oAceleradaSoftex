from abc import ABC, abstractmethod
from typing import Type

from CalculadoraInterativa import soma, sub, multi, divi


class Operations(ABC):

    @abstractmethod
    def operacoes(self):
        pass

    @abstractmethod
    def execute(self):
        pass

        class Soma(Operations):

            def __init__(self, execute):
                self.execute = execute

            def somar(self, soma, x, y):
                soma = x + y
                print('')
                print(f'A soma de {x} e {y} é {soma}')
                print('')

        class Subtracao(Operations):

            def __init__(self, execute):
                self.execute = execute

            def subtrair(self, sub):
                sub = x + y
                print('')
                print(f'A subtração de {x} e {y} é {sub}')
                print('')

        class Multiplicacao(Operations):

            def __init__(self, execute):
                self.execute = execute

            def multiplicar(self, multi):
                multi = x + y
                print('')
                print(f'A multiplicação de {x} e {y} é {multi}')
                print('')

        class Divisao(Operations):

            def __init__(self, execute):
                self.execute = execute

            def dividir(self, divi):
                divi = x + y
                print('')
                print(f'A divisão de {x} e {y} é {divi}')
                print('')

class Calculos:

    def __init__(self, operacoes: Type[Operations]):
        self.operacoes = operacoes

    def calcular(self):
        self.operacoes.execute()


if __name__ == "main":

    print('-------------------------------------')
    print(' Bem-vindo a Calculadora Interativa! ')
    print('-------------------------------------')
    print('')

digite = 5

while digite != 0:

    digite = int(input('    Digite aqui: '))
    if digite == 1:
        x = int(input('Digite o primeiro número - '))
        y = int(input('Agora o segundo número - '))
        soma.execute(x, y)

    elif digite == 2:
        x = int(input('Digite o primeiro número - '))
        y = int(input('Agora o segundo número - '))
        sub.execute(x, y)

    elif digite == 3:
        x = int(input('Digite o primeiro número - '))
        y = int(input('Agora o segundo número - '))
        multi.execute(x, y)

    elif digite == 4:
        x = int(input('Digite o primeiro número - '))
        y = int(input('Agora o segundo número - '))
        divi.execute(x, y)

    elif digite == 0:
        print('')
        print('Até a próxima!')
    else:
        print("Essa opção não existe! Tente novamente!")


