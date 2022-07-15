# Sistema Escolar
print('----------------------------------------')
print(' Questionário: Nome e Ano de Nascimento ')
print('----------------------------------------')

# Obrigar a pessoa a inserir um dado válido
while True:
    try:
        nome = input("Insira seu Nome Completo: ")
        ano = int(input("Digite o Ano de seu Nascimento: "))
    except ValueError:
        print('Valor incorreto. Favor inserir um caractere válido. ')


    if ano < 1922 and ano > 2022:
        print('Data incorreta. Favor inserir um ano entre 1922 e 2022')
        continue
    else:
        break

ano = 2022 - ano

print(f'{nome}! Você completará {ano} anos em 2022. Parabéns!')