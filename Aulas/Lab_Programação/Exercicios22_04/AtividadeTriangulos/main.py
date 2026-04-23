from entrada import listaTriangulo
from calculo import clasTriangulo

lista = listaTriangulo()
tipo, retangulo = clasTriangulo(lista)

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