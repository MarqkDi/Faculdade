def coletaValores():
    while True:
        try:
            notaProva = float(input('Insira a nota do aluno na prova: '))
            notaTrabalho = float(input('Insira a nota do aluno no trabalho: '))
            frequencia = int(input('Insira o percentual de frequência do aluno: '))
            if (notaProva > 10) or (notaProva < 0) or (notaTrabalho > 10) or (notaTrabalho < 0):
                print('')
                print('Valor da nota inválido (0 à 10)!')
                print('')
                continue
            if (frequencia > 100) or (frequencia < 0):
                print('')
                print('Percentual de frequência inválido (0 à 100)!')
                print('')
                continue
        except ValueError:
            print('')
            print('Insira apenas números!')
            print('')
        break
    return notaProva, notaTrabalho, frequencia