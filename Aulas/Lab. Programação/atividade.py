#Aula abud
#22/04/26

success = True
nomeVal = False

while True:
    nome = input('Digite o nome do aluno: ').capitalize()
    nomeVal = nome.isalpha()

    if nomeVal:
        break
    else:
        print('Digite apenas Letras!')
        continue

while True:
    try:
        matricula = int(input('Digite a matricula do aluno: '))
        while True:
            av1 = float(input('Digite a nota da primeira avaliação do aluno: '))
            av2 = float(input('Digite a nota da segunda avaliação do aluno: '))
            frequencia = int(input('Digite o percentual de frêquencia do aluno: '))
            if (av1 > 10) or (av2 > 10) or (av1 < 0) or (av2 < 0):
                print('Nota inválida!')
                continue
            elif (frequencia > 100) or (frequencia < 0):
                print('Valor de percentual inválido!')
                continue
            else:
                success = True
                break
        break

    except ValueError:
        print('Digite apenas valores!')
        continue

media = (av1 + av2) / 2

if (media >= 7) and (frequencia >= 75): situacao = 'Aprovado'
elif (media > 5) and (frequencia >= 75): situacao = 'Recuperação'
else: situacao = 'Reprovado'

if success:
    print(f'{"Resumo do Aluno":=^50}')
    print(f'Aluno: {" " * 10}{nome}')
    print(f'Matricula: {" " * 6}{matricula}')
    print(f'Avaliação 1: {" " * 4}{av1:.2f}')
    print(f'Avaliação 2: {" " * 4}{av2:.2f}')
    print('=' * 50)
    print(f'Situação: {" " * 7}{situacao}!')
    print(f'Média: {" " * 10}{media:.2f}')
    print('=' * 50)