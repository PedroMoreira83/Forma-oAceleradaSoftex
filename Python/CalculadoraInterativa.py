print('-------------------------------------')
print(' Bem-vindo a Calculadora Interativa! ')
print('-------------------------------------')
print('')

digite = 5
while digite != 0:
    print('''    Agora escolha um cálculo:
    
    Para "SOMA", aperte ---------- 1
    Para "SUBTRAÇÃO", aperte ----- 2
    Para "MULTIPLICAÇÃO", aperte - 3
    Para "DIVISÃO", aperte ------- 4
    Para "SAIR", aperte ---------- 0
    ''')
    digite = int(input('    Digite aqui: '))
    if digite == 1:
        print('')
        x = int(input('Digite o primeiro número - '))
        y = int(input('Agora o segundo número - '))
        soma = x + y
        print('')
        print(f'A soma de {x} e {y} é {soma}')
        print('')
    elif digite == 2:
        print('')
        x = int(input('Digite o primeiro número - '))
        y = int(input('Agora o segundo número - '))
        sub = x - y
        print('')
        print(f'A subtração de {x} e {y} é {sub}')
        print('')
    elif digite == 3:
        print('')
        x = int(input('Digite o primeiro número - '))
        y = int(input('Agora o segundo número - '))
        multi = x * y
        print('')
        print(f'A multiplicação de {x} e {y} é {multi}')
        print('')
    elif digite == 4:
        print('')
        x = int(input('Digite o primeiro número - '))
        y = int(input('Agora o segundo número - '))
        divi = x / y
        print('')
        print(f'A divisão de {x} e {y} é {divi}')
        print('')
    elif digite == 0:
        print('')
        print('Até a próxima!')
    else:
        print("Essa opção não existe! Tente novamente!")


