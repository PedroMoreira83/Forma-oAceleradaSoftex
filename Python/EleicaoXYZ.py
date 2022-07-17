import os


def votacao(candidato):  # fução para votação com a variavel candidato como argumento
    global candidato_x, candidato_y, candidato_z, voto_nulo, voto_branco

    if candidato.isalpha():  # checa se candidato contem apenas letras
        if candidato == 'Fim' or candidato == 'fim' or candidato == 'FIM':
            print('FIM DA VOTAÇÃO')
            print_resultados()
        else:
            print('Valor incorreto. Favor inserir o número de um candidato, ou "FIM" para sair')
            candidato

    elif candidato.isnumeric():  # checa se candidato e um caracter numerico
        if candidato == '889' or candidato == '847' or candidato == '515' or candidato == '0':
            if candidato == '889':
                while candidato:
                    candidato = str(input('Confirma(S/N)? '))
                    if candidato == 'S' or candidato == 's' or candidato == 'sim' or candidato == 'SIM':
                        print('Voto confirmado!')
                        candidato_x += 1
                        break
                    elif candidato == 'N' or candidato == 'n' or candidato == 'não' or candidato == 'NÃO':
                        return candidato
            elif candidato == '847':
                while candidato:
                    candidato = str(input('Confirma(S/N)? '))
                    if candidato == 'S' or candidato == 's' or candidato == 'sim' or candidato == 'SIM':
                        print('Voto confirmado!')
                        candidato_y += 1
                        break
                    elif candidato == 'N' or candidato == 'n' or candidato == 'não' or candidato == 'NÃO':
                        return candidato
            elif candidato == '515':
                while candidato:
                    candidato = str(input('Confirma(S/N)? '))
                    if candidato == 'S' or candidato == 's' or candidato == 'sim' or candidato == 'SIM':
                        print('Voto confirmado!')
                        candidato_z += 1
                        break
                    elif candidato == 'N' or candidato == 'n' or candidato == 'não' or candidato == 'NÃO':
                        return candidato
            elif candidato == '0':
                while candidato:
                    candidato = str(input('Confirma(S/N)? '))
                    if candidato == 'S' or candidato == 's' or candidato == 'sim' or candidato == 'SIM':
                        print('Voto Branco confirmado!')
                        voto_branco += 1
                        break
                    elif candidato == 'N' or candidato == 'n' or candidato == 'não' or candidato == 'NÃO':
                        return candidato
        elif candidato != '0' or candidato != '889' or candidato != '847' or candidato != '515':
            while candidato:
                candidato = str(input('Seu voto será anulado. Confirma(S/N)? '))
                if candidato == 'S' or candidato == 's' or candidato == 'sim' or candidato == 'SIM':
                    print('Seu voto foi anulado!')
                    voto_nulo += 1
                    break
        else:  # se o valor digitado nao e valido, há entrada de novo candidato e a funcao repete
            candidato


def print_resultados():  # printa resultados e encerra programa
    global candidato_x, candidato_y, candidato_z, voto_nulo

    print('QUANTIDADE DE VOTOS:\n')
    print('CANDIDATO X - TOTAL DE ' + str(candidato_x))
    print('CANDIDATO Y - TOTAL DE ' + str(candidato_y))
    print('CANDIDATO Z - TOTAL DE ' + str(candidato_z))
    print('VOTOS BRANCOS E NULOS - TOTAL DE ' + str(voto_nulo + voto_branco))
    exit()  # encerra prog


if __name__ == '__main__':  # funcao main
    candidato_x = 0
    candidato_y = 0
    candidato_z = 0
    voto_branco = 0
    voto_nulo = voto_branco + 0
    S = 0
    N = 0


    print('-----------------------------')
    print(' Eleições Eletrônicas Python ')
    print('-----------------------------')
    print('')
    print(f'Escolha Seu Candidato:{os.linesep}Para o candidato X, digite 889{os.linesep}Para o candidato Y, digite 847{os.linesep}Para o candidato Z, digite 515{os.linesep}Para Branco, digite 0')

    while True:  # laço ocorre indefinidamente ate que ocorra o 'Fim'
        candidato = str(input('Digite o numero do seu candidato: '))
        votacao(candidato)