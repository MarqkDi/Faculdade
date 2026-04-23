#Exercicio Abud 
#Data 22/04/26
from entrada import coletaValores
from aprovacao import calculoMedia, analiseSituacao

prova, trabalho, frequencia = coletaValores()
media = calculoMedia(prova, trabalho)
situacao = analiseSituacao(media, frequencia, trabalho)

print(f'{"Resumo Aluno":=^50}')
print(f'Nota na Prova: {" " * 5}{prova:.2f}')
print(f'Nota no Trabalho: {" " * 2}{trabalho:.2f}')
print(f'Frequência: {" " * 8}{frequencia}')
print(f'Média: {" " * 13}{media:.2f}')
print(f'Situação: {" " * 7}{situacao}')
print(f'{"=" * 50}')