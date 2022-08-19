import pandas as pd

# Sistema Escolar
print('-------------------------------------')
print(' Sistema de Verificação de Aprovação ')
print('-------------------------------------')

nome = input('Digite o nome do aluno: ')

# Obrigar a pessoa a inserir um dado válido
while True:
    try:
        n1 = float(input("Primeira Nota: "))
        n2 = float(input("Segunda Nota: "))
    except ValueError:
        print('Dado incorreto. Favor inserir um valor entre 0 e 10')


# Impedindo números maiores que 10, ou negativos.
    if n1 > 10.0 or n1 < 0:
        print('Nota incorreta. Favor inserir valores entre 0 e 10')
        continue
    elif n2 > 10.0 or n2 < 0:
        print('Nota incorreta. Favor inserir valores entre 0 e 10')
        continue
    else:
        break

# Inserir o número de faltas
while True:
    try:
        faltas = int(input("Digite número de faltas: "))
    except ValueError:
        print('Valor incorreto. Insira um número inteiro')
    break

m = (n1 + n2) /2

if m >= 7.0 and m <= 10.0:
    if faltas <= 3:
        print(f'O(A) aluno(a) {nome} obteve média {m}. Aprovado(a)!')
    elif m >=7 and faltas > 3:
        print(f'Embora média do(a) aluno(a) {nome} seja {m}, seu número de faltas excede o mínimo de 3. Infelizmente está reprovado(a)!')
    else:
        print(f'O número de faltas do(a) aluno(a) {nome} excede o mínimo de 3. Infelizmente está reprovado(a)!')
else:
    print(f'O(A) aluno(a) {nome} obteve média {m}. Infelizmente está reprovado(a)!')


tabela1 = pd.read_csv('notas_alunos.csv')

print(tabela1)




