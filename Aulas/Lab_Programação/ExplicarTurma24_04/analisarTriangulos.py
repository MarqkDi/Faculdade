#Uma forma diferente de entrada de valores, trabalhando com listas, validação de quantidade de números inseridos, e organização
""" 
while True:
    entrada = input('Digite os três valores separados por espaço: ')
    lista = entrada.split()
    if len(lista) != 3:
        print('Digite exatamente 3 valores!')
        continue

    listaFlo = []

    for item in lista:
        listaFlo.append(float(item))
    listaFlo = sorted(listaFlo)
    break
"""

#Metódo mais simples de entrada, sem usar listas
a = float(input('Digite o primeiro valor: '))
b = float(input('Digite o segundo valor: '))
c = float(input('Digite o terceiro valor: '))

#Aqui complica um pouco que é onde vamos fazer todos os cálculos e condições
retangulo = False

lista = sorted([a, b, c])
if ((lista[0] + lista[1]) > lista[2]):
        if ((lista[0] ** 2) + (lista[1] ** 2)) == (lista[2] ** 2):
                retangulo = True
        if lista[0] == lista[1] == lista[2]: 
            tipo = 'Equilátero'
        elif (lista[0] == lista[1]) or (lista[0] == lista[2]) or (lista[1] == lista[2]):
            tipo = 'Isóceles'
        else:
            tipo = 'Escaleno'

elif (lista[0] + lista[1]) == lista[2]:
    tipo = 'Degenerado'
else: 
    tipo = None

#Saidas
print(f'{"Resumão do Triângulo":=^63} \n')

if tipo is None:
    print('Não é possível formar um triângulo, nem um segmento degenerado!')

elif tipo == 'Degenerado':
    print('Não é possível criar um triângulo, porém é possível formar um segmento degenerado!')

else:
    print('É possível criar um triângulo!')

    if retangulo:
        print('É um triângulo retângulo!')
    else:
        print('Não é um triângulo retângulo!')

    print(f'Tipo do triângulo: {tipo}')

print('')
print('\n' + '=' * 63)