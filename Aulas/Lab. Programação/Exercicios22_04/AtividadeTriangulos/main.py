from entrada import listaTriangulo
from calculo import clasTriangulo

lista = listaTriangulo()
triangulo, retangulo = clasTriangulo(lista)

print(f'{"Resumão do Triângulo":=^63}')
print('')
if triangulo is not None:

    if triangulo != True:

        print('É possível criar um triângulo!')

        if retangulo:
            print('É um triângulo retângulo!')
        else:
            print('Não é um triângulo retângulo!')

        print(f'Tipo do triângulo: {triangulo}')

    else:
        print('Não é possível criar um triângulo, porém é possível formar um segmento degenerado!')

else:
    print('Não é possível formar um triângulo, nem um segmento degenerado!')

print('')
print(f'{"=" * 63}')