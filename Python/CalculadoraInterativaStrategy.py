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
