valor = int(input('Digite um valor: '))

#Verificação de natureza do valor
if valor > 0: 
    natureza = 'Positiva'
elif valor < 0:
    natureza = 'Negativa'
else:
    natureza ='Neutra'

#Verificação se é ou não par
if valor % 2 == 0:
    parImp = 'Par'
else:
    parImp = 'Ímpar'

#Verificação dos múltiplos
mult3 = False
mult5 = False
mult7 = False

if valor % 3 == 0: 
    mult3 = True
if valor % 5 == 0: 
    mult5 = True
if valor % 7 == 0: 
    mult7 = True

#Condições especiais
if mult3 and mult5 and mult7: 
    condEsp = 'Número Raro'
elif mult3 and mult5 and not mult7: 
    condEsp = 'FizzBuzz Especial'
elif (natureza == 'Negativa') and (parImp == 'Par'): 
    condEsp = 'Número negativo, Par problemático'
else: 
    condEsp = None

#Saída de valores
print(f'{"Resumão do Valor":=^50}')
print(f'Seu valor é {parImp}')
print(f'E tem uma natureza {natureza}')
if mult3:
    print('É múltiplo de 3!')
if mult5:
    print('É múltiplo de 5!')
if mult7:
    print('É múltiplo de 7!')
if condEsp is not None:
    print(f'Parabéns você conseguiu um {condEsp}!')
else:
    print('Infelizmente seu número não tem nenhuma condição especial :(')