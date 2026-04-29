while True:
    valor = int(input('Digite um valor de 0 a 10: '))
    if (valor < 0) or (valor > 10):
        print('Valor inválido')
        continue
    else:
        print('Valor válido')
        break