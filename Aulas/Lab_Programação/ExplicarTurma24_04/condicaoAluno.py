#Loop pra aceitar apenas valores válidos
while True:    
    notaProva = float(input('Insira a nota do aluno na prova: '))
    notaTrabalho = float(input('Insira a nota do aluno no trabalho: '))
    frequencia = int(input('Insira o percentual de frequência do aluno: '))
    
    #Condições responsáveis por verificar apenas numéros validos
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
    break

#Cálculo da média
media = ((notaProva * 0.7) + (notaTrabalho * 0.3))

#Condições de aprovação
if (media >= 8) and (frequencia >= 90):
    situacao = 'Aprovado com Mérito!'
elif (media >= 7) and (frequencia >= 75):
    situacao = 'Aprovado direto!'
elif (media < 5) and (notaTrabalho >= 8):
    situacao = 'Reprovado com bom desempenho em trabalho!'
elif ((media > 5) and (media < 7)) or ((frequencia > 60) and (frequencia < 74)):
    situacao = 'Recuperação!'
else:
    situacao = 'Reprovado!'

#Comandos de saída
print(f'{"Resumo Aluno":=^50}')
print(f'Nota na Prova: {" " * 5}{notaProva:.2f}')
print(f'Nota no Trabalho: {" " * 2}{notaTrabalho:.2f}')
print(f'Frequência: {" " * 8}{frequencia}%')
print(f'Média: {" " * 13}{media:.2f}')
print(f'Situação: {" " * 7}{situacao}')
print(f'{"=" * 50}')