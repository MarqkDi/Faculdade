def coletarTipo():
    while True:
        print('1 - Comum \n2 - Vip \n3 - Funcionário')
        tipoCliente = int(input('Qual tipo de cliente você é?: '))
        if tipoCliente not in [1, 2, 3]:
            print('Opção inválida!')
            continue
        break
    
    if tipoCliente == 1: return 'Comum'
    elif tipoCliente == 2: return 'Vip'
    else: return 'Funcionário'

def valCompra():
    while True:
        try:
            valor = float(input('Digite o valor da compra: R$'))
        except ValueError:
            print('Digite apenas números!')
            continue
        break
    return valor