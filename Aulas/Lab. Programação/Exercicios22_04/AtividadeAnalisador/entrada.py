def coletarValor():
    while True:
        try:
            valor = int(input('Digite um valor: '))
        except ValueError:
            print('')
            print('Apenas números!')
            print('')
            continue
        break
    return valor