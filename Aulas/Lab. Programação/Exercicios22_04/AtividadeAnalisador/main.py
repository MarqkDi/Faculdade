#Atividade Abud
#22/04/26

from entrada import coletarValor
from calculo import natureza, par, multiplo
from condicoes import analise

valor = coletarValor()
mult3, mult5, mult7 = multiplo(valor)
parImp = par(valor)
inteiros = natureza(valor)
raridade = analise(mult3, mult5, mult7, parImp, inteiros)

print(f'{"Resumão do Valor":=^50}')
print(f'Seu valor é {parImp}')
print(f'E tem uma natureza {inteiros}')
if mult3:
    print('É múltiplo de 3!')
if mult5:
    print('É múltiplo de 5!')
if mult7:
    print('É múltiplo de 7!')
if raridade is not None:
    print(f'Parabéns você conseguiu um {raridade}!')
else:
    print('Infelizmente seu número não tem nenhuma condição especial :(')